from datetime import datetime, date

from dateutil.parser import parse

from base_model.tools import get_class_name, parse_quotes


class AttributeValidation:
    DATE_FORMATS = [
        '%Y-%m-%d',
        '%d/%m/%Y'
    ]
    DATETIME_FORMATS = [
        '%Y-%m%dT%H:%M:%S',
        '%Y-%m%dT%H:%M:%S.%f',
        '%Y-%m%dT%H:%M:%S.%f%z',
        '%Y-%m%d %H:%M:%S',
        '%Y-%m%d %H:%M:%S.%f',
        '%Y-%m%d %H:%M:%S.%f%z',
        '%d/%m/%Y %H:%M:%S'
    ]

    def __init__(self, model_class, attribute_name: str, attribute_type, list_of=None):
        self._model_class = model_class
        self._attribute = attribute_name
        self._type = attribute_type
        self._required = False
        self._extra = None
        self._default = lambda instance: None
        self._list_of = list_of

    @property
    def is_required(self):
        return self._required

    def set_extra_validations(self, extra):
        """
        Extra validations must be space delimited

        required
        default=expression
        """
        for validation in parse_quotes(extra):
            if validation.upper() == 'REQUIRED':
                self._required = True
            elif validation.upper().startswith('DEFAULT='):
                self.set_default(validation.split('=')[1])

        return True

    def set_default(self, default_expression):
        """
        Set default value for reset or init


        """
        if default_expression is None or default_expression == "None":
            self._default = lambda instance: None
            return

        if "self." in default_expression:
            self._default = eval("lambda instance: instance" + default_expression[4:])
        elif default_expression == "MIN_TIMESTAMP":
            if self._type == datetime:
                self._default = lambda instance: datetime(1970, 1, 1, 0, 0, 0, 0)
            elif self._type == date:
                self._default = lambda instance: date(1970, 1, 1)
        else:
            self._default = eval("lambda instance: " + default_expression)

    def get_default(self, model_instance):
        return self._default(model_instance)

    def normalize_data(self, value):
        if isinstance(value, self._type):
            return True, value
        if self._type == date:
            success, value = self._normalize_date(value)
        elif self._type == datetime:
            success, value = self._normalize_datetime(value)
        else:
            try:
                value = self._type(value)
                success = True
            except:
                success = False

        return success, value

    def _normalize_date(self, value) -> date:
        for format in self.DATE_FORMATS:
            try:
                _date = datetime.strptime(value, format)
                return True, _date.date()
            except:
                # try another
                pass
        try:
            _date = parse(value)
            return True, _date.date()
        except:
            return False, None

    def _normalize_datetime(self, value):
        for format in self.DATETIME_FORMATS:
            try:
                _date = datetime.strptime(value, format)
                return True, _date
            except:
                # try another
                pass
        try:
            _date = parse(value)
            return True, _date
        except:
            return False, None

    def __str__(self):
        return "{0}.{1}:{2} ({3})".format(
            get_class_name(self._model_class),
            self._attribute,
            str(self._type),
            self._extra)

    def __repr__(self):
        return str(self)
