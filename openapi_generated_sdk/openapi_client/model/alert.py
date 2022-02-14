"""
    Thousand Eyes API V6

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 6.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from openapi_client.exceptions import ApiAttributeError


def lazy_import():
    from openapi_client.model.alert_agent_obj import AlertAgentObj
    from openapi_client.model.alert_api_links import AlertApiLinks
    from openapi_client.model.alert_monitor_obj import AlertMonitorObj
    globals()['AlertAgentObj'] = AlertAgentObj
    globals()['AlertApiLinks'] = AlertApiLinks
    globals()['AlertMonitorObj'] = AlertMonitorObj


class Alert(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('active',): {
            '0': 0,
            '1': 1,
            '2': 2,
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'alert_id': (int,),  # noqa: E501
            'test_id': (int,),  # noqa: E501
            'rule_id': (int,),  # noqa: E501
            'test_name': (str,),  # noqa: E501
            'active': (int,),  # noqa: E501
            'rule_expression': (str,),  # noqa: E501
            'date_start': (datetime,),  # noqa: E501
            'date_end': (datetime,),  # noqa: E501
            'violation_count': (int,),  # noqa: E501
            'rule_name': (str,),  # noqa: E501
            'permalink': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'agents': ([AlertAgentObj],),  # noqa: E501
            'monitors': ([AlertMonitorObj],),  # noqa: E501
            'api_links': ([AlertApiLinks],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'alert_id': 'alertId',  # noqa: E501
        'test_id': 'testId',  # noqa: E501
        'rule_id': 'ruleId',  # noqa: E501
        'test_name': 'testName',  # noqa: E501
        'active': 'active',  # noqa: E501
        'rule_expression': 'ruleExpression',  # noqa: E501
        'date_start': 'dateStart',  # noqa: E501
        'date_end': 'dateEnd',  # noqa: E501
        'violation_count': 'violationCount',  # noqa: E501
        'rule_name': 'ruleName',  # noqa: E501
        'permalink': 'permalink',  # noqa: E501
        'type': 'type',  # noqa: E501
        'agents': 'agents',  # noqa: E501
        'monitors': 'monitors',  # noqa: E501
        'api_links': 'apiLinks',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Alert - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            alert_id (int): unique ID of the alert; each alert occurrence is assigned a new unique ID. [optional]  # noqa: E501
            test_id (int): unique ID of the test (see `/tests/{testId}` endpoint for more detail). [optional]  # noqa: E501
            rule_id (int): unique ID of the alert rule (see `/alert-rules` endpoint for more detail). [optional]  # noqa: E501
            test_name (str): name of the test. [optional]  # noqa: E501
            active (int): 0 for inactive, 1 for active, 2 for disabled. Alert is disabled if either alert rule itself has been deleted or the test it is applied to has been disabled, deleted, disabled alerting, or disassociated the alert rule from the test. [optional]  # noqa: E501
            rule_expression (str): string expression of alert rule. [optional]  # noqa: E501
            date_start (datetime): the date/time where an alert rule was triggered, expressed in UTC. [optional]  # noqa: E501
            date_end (datetime): the date/time where the alert was marked as cleared, expressed in UTC. [optional]  # noqa: E501
            violation_count (int): number of sources currently meeting the alert criteria. [optional]  # noqa: E501
            rule_name (str): name of the alert rule. [optional]  # noqa: E501
            permalink (str): hyperlink to alerts list, with row expanded. [optional]  # noqa: E501
            type (str): type of alert being triggered. [optional]  # noqa: E501
            agents ([AlertAgentObj]): array of agents where the alert has at some point been active since the point that the alert was triggered. Not shown on BGP alerts.. [optional]  # noqa: E501
            monitors ([AlertMonitorObj]): array of agents where the alert has at some point been active since the point that the alert was triggered. Not shown on BGP alerts.. [optional]  # noqa: E501
            api_links ([AlertApiLinks]): list of hyperlinks to other areas of the API. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Alert - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            alert_id (int): unique ID of the alert; each alert occurrence is assigned a new unique ID. [optional]  # noqa: E501
            test_id (int): unique ID of the test (see `/tests/{testId}` endpoint for more detail). [optional]  # noqa: E501
            rule_id (int): unique ID of the alert rule (see `/alert-rules` endpoint for more detail). [optional]  # noqa: E501
            test_name (str): name of the test. [optional]  # noqa: E501
            active (int): 0 for inactive, 1 for active, 2 for disabled. Alert is disabled if either alert rule itself has been deleted or the test it is applied to has been disabled, deleted, disabled alerting, or disassociated the alert rule from the test. [optional]  # noqa: E501
            rule_expression (str): string expression of alert rule. [optional]  # noqa: E501
            date_start (datetime): the date/time where an alert rule was triggered, expressed in UTC. [optional]  # noqa: E501
            date_end (datetime): the date/time where the alert was marked as cleared, expressed in UTC. [optional]  # noqa: E501
            violation_count (int): number of sources currently meeting the alert criteria. [optional]  # noqa: E501
            rule_name (str): name of the alert rule. [optional]  # noqa: E501
            permalink (str): hyperlink to alerts list, with row expanded. [optional]  # noqa: E501
            type (str): type of alert being triggered. [optional]  # noqa: E501
            agents ([AlertAgentObj]): array of agents where the alert has at some point been active since the point that the alert was triggered. Not shown on BGP alerts.. [optional]  # noqa: E501
            monitors ([AlertMonitorObj]): array of agents where the alert has at some point been active since the point that the alert was triggered. Not shown on BGP alerts.. [optional]  # noqa: E501
            api_links ([AlertApiLinks]): list of hyperlinks to other areas of the API. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
