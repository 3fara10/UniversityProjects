class ValidationException(Exception):
    def __init__(self, field_name: str):
        self.__field_name = field_name

    def get_field_name(self):
        #return the field name that makes the exception
        return self.__field_name
