import inspect
import typing

from base_model.attribute_validation import AttributeValidation
from base_model.base_model_exception import BaseModelException
from base_model.tools import get_class_name


class BaseModelValidation:
    VALIDATIONS = {}

    def __init__(self, model_class):

        self._class_name = get_class_name(model_class)
        self._model_class = model_class
        _members = ([x[1] for x in inspect.getmembers(model_class)
                     if x[0] == '__annotations__'] + [None])[0]
        if not _members:
            raise BaseModelException(
                f"Class {self._class_name} has no typed declared members")

        _validations = {}
        _type_hints = typing.get_type_hints(model_class)

        for member in _members:
            _member_type = _members[member]
            _list_of = None
            if issubclass(_member_type, typing.List):
                _list_of = self._get_list_of(_member_type)
                if _list_of is None:
                    raise BaseModelException("Invalid type hint {0} for field {1} of model {2}".format(
                        _member_type,
                        member,
                        self._class_name
                    ))

            _validations[member] = AttributeValidation(
                model_class=model_class.__class__,
                attribute_name=member,
                attribute_type=_member_type,
                list_of=_list_of)

        self._attributes_validations = _validations
        self._get_extra_validations()
        self._members = _members

    def get_attribute_validation(self, field_name):
        if field_name in self._attributes_validations:
            return self._attributes_validations[field_name]
        return None

    def __str__(self):
        return "Validation {0}: {1}".format(
            self._class_name,
            self._attributes_validations
        )

    def get_fields(self) -> list:
        """
        Returns list of field names
        """
        return [member for member in self._members]

    def get_field_type(self, field_name):
        if field_name not in self._members:
            raise BaseModelException("Field name {0} not found in model {1}".format(
                field_name,
                self._class_name))

        return self._members[field_name]

    def get_field_default_value(self, field_name, model_instance):
        if field_name in self._members:
            validation: AttributeValidation = self._attributes_validations[field_name]
            return validation.get_default(model_instance)
        return None

    @classmethod
    def get_validation(cls, model_class):
        cn = get_class_name(model_class)
        if cn not in cls.VALIDATIONS:
            validation = BaseModelValidation(model_class)
            cls.VALIDATIONS[cn] = validation

        return cls.VALIDATIONS[cn]

    def _get_extra_validations(self):
        _docs = inspect.getdoc(self._model_class)
        if not isinstance(_docs, str):
            return
        for doc in _docs.splitlines():
            details = doc.strip().split(':')
            if len(details) > 1:
                attr_name = details[0].strip()
                if attr_name in self._attributes_validations:
                    attr_props = ' '.join([d.strip() for d in details[1:]])
                    self._attributes_validations[attr_name].set_extra_validations(attr_props)

    def _get_list_of(self, field_type):
        try:
            type_of_list = field_type.__args__
        except:
            type_of_list = None
        return type_of_list
