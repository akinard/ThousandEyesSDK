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
    from openapi_client.model.base_test import BaseTest
    from openapi_client.model.base_test_alert_rules import BaseTestAlertRules
    from openapi_client.model.base_test_api_links import BaseTestApiLinks
    from openapi_client.model.base_test_shared_with_accounts import BaseTestSharedWithAccounts
    from openapi_client.model.group import Group
    from openapi_client.model.shareable_test_all_of import ShareableTestAllOf
    from openapi_client.model.test_type import TestType
    globals()['BaseTest'] = BaseTest
    globals()['BaseTestAlertRules'] = BaseTestAlertRules
    globals()['BaseTestApiLinks'] = BaseTestApiLinks
    globals()['BaseTestSharedWithAccounts'] = BaseTestSharedWithAccounts
    globals()['Group'] = Group
    globals()['ShareableTestAllOf'] = ShareableTestAllOf
    globals()['TestType'] = TestType


class ShareableTest(ModelComposed):
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
    }

    validations = {
        ('test_id',): {
            'inclusive_minimum': 1,
        },
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
            'alerts_enabled': (bool,),  # noqa: E501
            'alert_rules': ([BaseTestAlertRules],),  # noqa: E501
            'api_links': ([BaseTestApiLinks],),  # noqa: E501
            'created_by': (str,),  # noqa: E501
            'created_date': (datetime,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'enabled': (bool,),  # noqa: E501
            'groups': ([Group],),  # noqa: E501
            'modified_by': (str,),  # noqa: E501
            'modified_date': (datetime,),  # noqa: E501
            'saved_event': (bool,),  # noqa: E501
            'shared_with_accounts': ([BaseTestSharedWithAccounts],),  # noqa: E501
            'test_id': (int,),  # noqa: E501
            'test_name': (str,),  # noqa: E501
            'type': (TestType,),  # noqa: E501
            'live_share': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'alerts_enabled': 'alertsEnabled',  # noqa: E501
        'alert_rules': 'alertRules',  # noqa: E501
        'api_links': 'apiLinks',  # noqa: E501
        'created_by': 'createdBy',  # noqa: E501
        'created_date': 'createdDate',  # noqa: E501
        'description': 'description',  # noqa: E501
        'enabled': 'enabled',  # noqa: E501
        'groups': 'groups',  # noqa: E501
        'modified_by': 'modifiedBy',  # noqa: E501
        'modified_date': 'modifiedDate',  # noqa: E501
        'saved_event': 'savedEvent',  # noqa: E501
        'shared_with_accounts': 'sharedWithAccounts',  # noqa: E501
        'test_id': 'testId',  # noqa: E501
        'test_name': 'testName',  # noqa: E501
        'type': 'type',  # noqa: E501
        'live_share': 'liveShare',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ShareableTest - a model defined in OpenAPI

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
            alerts_enabled (bool): choose 1 to enable alerts, or 0 to disable alerts. Defaults to 1. [optional]  # noqa: E501
            alert_rules ([BaseTestAlertRules]): array of alert rule objects `{\"ruleId\": ruleId}`; get ruleId from `/alert-rules` endpoint. If alertsEnabled is set to 1 and alertRules is not included in a creation/update query, applicable defaults will be used.. [optional]  # noqa: E501
            api_links ([BaseTestApiLinks]): array of apiLinks objects, showing rel and href elements; Read only; self links to endpoint to pull test metadata, and data links to endpoint for test data. [optional]  # noqa: E501
            created_by (str): Username (email@company.com); read only. [optional]  # noqa: E501
            created_date (datetime): YYYY-MM-DD HH:mm:ss formatted date; read only; shown in UTC. [optional]  # noqa: E501
            description (str): defaults to empty string. [optional]  # noqa: E501
            enabled (bool): choose 1 to enable the test, 0 to disable the test. [optional]  # noqa: E501
            groups ([Group]): array of label objects (`\"groups\": [ { \"name\": \"groupName\", \"groupId\": groupId, \"builtIn\": 0}]`); get groupId from /groupsendpoint.. [optional]  # noqa: E501
            modified_by (str): Username (email@company.com); read only. [optional]  # noqa: E501
            modified_date (datetime): YYYY-MM-DD HH:mm:ss formatted date; read only; shown in UTC. [optional]  # noqa: E501
            saved_event (bool): read only; indicates 1 for a saved event, 0 for a normal test. [optional]  # noqa: E501
            shared_with_accounts ([BaseTestSharedWithAccounts]): array of account group objects (`\"sharedWithAccounts\": [{\"aid\": aid, \"name\": \"AccountGroupName\"}]`); Test is shared with the listed accout groups. Get aid and name from account-groups endpoint.. [optional]  # noqa: E501
            test_id (int): unique ID of test; read only; each test is assigned a unique ID; this is used to access test data from other endpoints.. [optional]  # noqa: E501
            test_name (str): Test name must be unique. [optional]  # noqa: E501
            type (TestType): [optional]  # noqa: E501
            live_share (bool): read only; indicates 1 for a test shared with your account group, 0 for a normal test. [optional]  # noqa: E501
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
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
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ShareableTest - a model defined in OpenAPI

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
            alerts_enabled (bool): choose 1 to enable alerts, or 0 to disable alerts. Defaults to 1. [optional]  # noqa: E501
            alert_rules ([BaseTestAlertRules]): array of alert rule objects `{\"ruleId\": ruleId}`; get ruleId from `/alert-rules` endpoint. If alertsEnabled is set to 1 and alertRules is not included in a creation/update query, applicable defaults will be used.. [optional]  # noqa: E501
            api_links ([BaseTestApiLinks]): array of apiLinks objects, showing rel and href elements; Read only; self links to endpoint to pull test metadata, and data links to endpoint for test data. [optional]  # noqa: E501
            created_by (str): Username (email@company.com); read only. [optional]  # noqa: E501
            created_date (datetime): YYYY-MM-DD HH:mm:ss formatted date; read only; shown in UTC. [optional]  # noqa: E501
            description (str): defaults to empty string. [optional]  # noqa: E501
            enabled (bool): choose 1 to enable the test, 0 to disable the test. [optional]  # noqa: E501
            groups ([Group]): array of label objects (`\"groups\": [ { \"name\": \"groupName\", \"groupId\": groupId, \"builtIn\": 0}]`); get groupId from /groupsendpoint.. [optional]  # noqa: E501
            modified_by (str): Username (email@company.com); read only. [optional]  # noqa: E501
            modified_date (datetime): YYYY-MM-DD HH:mm:ss formatted date; read only; shown in UTC. [optional]  # noqa: E501
            saved_event (bool): read only; indicates 1 for a saved event, 0 for a normal test. [optional]  # noqa: E501
            shared_with_accounts ([BaseTestSharedWithAccounts]): array of account group objects (`\"sharedWithAccounts\": [{\"aid\": aid, \"name\": \"AccountGroupName\"}]`); Test is shared with the listed accout groups. Get aid and name from account-groups endpoint.. [optional]  # noqa: E501
            test_id (int): unique ID of test; read only; each test is assigned a unique ID; this is used to access test data from other endpoints.. [optional]  # noqa: E501
            test_name (str): Test name must be unique. [optional]  # noqa: E501
            type (TestType): [optional]  # noqa: E501
            live_share (bool): read only; indicates 1 for a test shared with your account group, 0 for a normal test. [optional]  # noqa: E501
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              BaseTest,
              ShareableTestAllOf,
          ],
          'oneOf': [
          ],
        }
