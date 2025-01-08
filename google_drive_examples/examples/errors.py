from enum import Enum


__all__ = [
    'ArgumentError',
]


class _Type(Enum):
    """[Error Sub-Types]
    :Key: <sub-type>
    :Value: <message-format>
    """
    VALUE_TYPE_ERROR = "for ({argument}) , Expected value : {expected}, Got value : {got}. {additional_message}"
    VALUE_VALIDATION_ERROR = "for ({argument}), {additional_message}"


class ArgumentError(Exception):
    f"""[If Argument (class/method/function) is incorrect]
    
    :param originator_name: name of class/menthod/funtion that raised error
    :type  originator_name: str

    :param _type: type of argument error . options {_Type._member_names_}
    :type  _type: (Enum _Type)

    :param _message: description/details about the error .
                     Suggested to compy (Enum _Type) value format .
    :type  _message: str
    """
    def __init__(self, *args, originator_name:str, _type:_Type, _message: str):
        super().__init__(*args)
        self._originator_name= originator_name
        self._type= _type
        self._message= f"{self.__class__.__name__} | {_type.name} | in `{self._originator_name}`" + " : " + _message

    def __str__(self) -> str:
        return self._message
