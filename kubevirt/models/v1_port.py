# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1Port(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'port': 'int',
        'protocol': 'str'
    }

    attribute_map = {
        'name': 'name',
        'port': 'port',
        'protocol': 'protocol'
    }

    def __init__(self, name=None, port=None, protocol=None):
        """
        V1Port - a model defined in Swagger
        """

        self._name = None
        self._port = None
        self._protocol = None

        if name is not None:
          self.name = name
        self.port = port
        if protocol is not None:
          self.protocol = protocol

    @property
    def name(self):
        """
        Gets the name of this V1Port.
        If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services. +optional

        :return: The name of this V1Port.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1Port.
        If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services. +optional

        :param name: The name of this V1Port.
        :type: str
        """

        self._name = name

    @property
    def port(self):
        """
        Gets the port of this V1Port.
        Number of port to expose for the virtual machine. This must be a valid port number, 0 < x < 65536.

        :return: The port of this V1Port.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this V1Port.
        Number of port to expose for the virtual machine. This must be a valid port number, 0 < x < 65536.

        :param port: The port of this V1Port.
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")

        self._port = port

    @property
    def protocol(self):
        """
        Gets the protocol of this V1Port.
        Protocol for port. Must be UDP or TCP. Defaults to \"TCP\". +optional

        :return: The protocol of this V1Port.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this V1Port.
        Protocol for port. Must be UDP or TCP. Defaults to \"TCP\". +optional

        :param protocol: The protocol of this V1Port.
        :type: str
        """

        self._protocol = protocol

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1Port):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
