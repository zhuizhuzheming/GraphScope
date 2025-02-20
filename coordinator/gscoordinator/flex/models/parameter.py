from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from gscoordinator.flex.models.base_model import Model
from gscoordinator.flex.models.gs_data_type import GSDataType
from gscoordinator.flex import util

from gscoordinator.flex.models.gs_data_type import GSDataType  # noqa: E501

class Parameter(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, type=None, allow_cast=None):  # noqa: E501
        """Parameter - a model defined in OpenAPI

        :param name: The name of this Parameter.  # noqa: E501
        :type name: str
        :param type: The type of this Parameter.  # noqa: E501
        :type type: GSDataType
        :param allow_cast: The allow_cast of this Parameter.  # noqa: E501
        :type allow_cast: bool
        """
        self.openapi_types = {
            'name': str,
            'type': GSDataType,
            'allow_cast': bool
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'allow_cast': 'allow_cast'
        }

        self._name = name
        self._type = type
        self._allow_cast = allow_cast

    @classmethod
    def from_dict(cls, dikt) -> 'Parameter':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Parameter of this Parameter.  # noqa: E501
        :rtype: Parameter
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Parameter.


        :return: The name of this Parameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Parameter.


        :param name: The name of this Parameter.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self) -> GSDataType:
        """Gets the type of this Parameter.


        :return: The type of this Parameter.
        :rtype: GSDataType
        """
        return self._type

    @type.setter
    def type(self, type: GSDataType):
        """Sets the type of this Parameter.


        :param type: The type of this Parameter.
        :type type: GSDataType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def allow_cast(self) -> bool:
        """Gets the allow_cast of this Parameter.


        :return: The allow_cast of this Parameter.
        :rtype: bool
        """
        return self._allow_cast

    @allow_cast.setter
    def allow_cast(self, allow_cast: bool):
        """Sets the allow_cast of this Parameter.


        :param allow_cast: The allow_cast of this Parameter.
        :type allow_cast: bool
        """

        self._allow_cast = allow_cast
