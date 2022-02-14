"""
    Thousand Eyes API V6

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 6.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.group_type import GroupType
from openapi_client.model.inline_object import InlineObject
from openapi_client.model.inline_object1 import InlineObject1
from openapi_client.model.inline_response2008 import InlineResponse2008
from openapi_client.model.inline_response2009 import InlineResponse2009
from openapi_client.model.inline_response201 import InlineResponse201


class LabelsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.groups_get_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse2008,),
                'auth': [
                    'basicAuth',
                    'bearerAuth'
                ],
                'endpoint_path': '/groups',
                'operation_id': 'groups_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'aid',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'aid':
                        (int,),
                },
                'attribute_map': {
                    'aid': 'aid',
                },
                'location_map': {
                    'aid': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.groups_group_id_delete_post_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth',
                    'bearerAuth'
                ],
                'endpoint_path': '/groups/{groupId}/delete',
                'operation_id': 'groups_group_id_delete_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'group_id',
                    'aid',
                ],
                'required': [
                    'group_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'group_id':
                        (int,),
                    'aid':
                        (int,),
                },
                'attribute_map': {
                    'group_id': 'groupId',
                    'aid': 'aid',
                },
                'location_map': {
                    'group_id': 'path',
                    'aid': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.groups_group_id_get_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse2009,),
                'auth': [
                    'basicAuth',
                    'bearerAuth'
                ],
                'endpoint_path': '/groups/{groupId}',
                'operation_id': 'groups_group_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'group_id',
                    'aid',
                ],
                'required': [
                    'group_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'group_id':
                        (int,),
                    'aid':
                        (int,),
                },
                'attribute_map': {
                    'group_id': 'groupId',
                    'aid': 'aid',
                },
                'location_map': {
                    'group_id': 'path',
                    'aid': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.groups_group_id_update_post_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse201,),
                'auth': [
                    'basicAuth',
                    'bearerAuth'
                ],
                'endpoint_path': '/groups/{groupId}/update',
                'operation_id': 'groups_group_id_update_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'group_id',
                    'inline_object1',
                    'aid',
                ],
                'required': [
                    'group_id',
                    'inline_object1',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'group_id':
                        (int,),
                    'inline_object1':
                        (InlineObject1,),
                    'aid':
                        (int,),
                },
                'attribute_map': {
                    'group_id': 'groupId',
                    'aid': 'aid',
                },
                'location_map': {
                    'group_id': 'path',
                    'inline_object1': 'body',
                    'aid': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.groups_type_get_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse2008,),
                'auth': [
                    'basicAuth',
                    'bearerAuth'
                ],
                'endpoint_path': '/groups/{type}',
                'operation_id': 'groups_type_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'type',
                    'aid',
                ],
                'required': [
                    'type',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'type':
                        (GroupType,),
                    'aid':
                        (int,),
                },
                'attribute_map': {
                    'type': 'type',
                    'aid': 'aid',
                },
                'location_map': {
                    'type': 'path',
                    'aid': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.groups_type_group_id_get_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse2009,),
                'auth': [
                    'basicAuth',
                    'bearerAuth'
                ],
                'endpoint_path': '/groups/{type}/{groupId}',
                'operation_id': 'groups_type_group_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'type',
                    'group_id',
                    'aid',
                ],
                'required': [
                    'type',
                    'group_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'type':
                        (GroupType,),
                    'group_id':
                        (int,),
                    'aid':
                        (int,),
                },
                'attribute_map': {
                    'type': 'type',
                    'group_id': 'groupId',
                    'aid': 'aid',
                },
                'location_map': {
                    'type': 'path',
                    'group_id': 'path',
                    'aid': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.groups_type_new_post_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse201,),
                'auth': [
                    'basicAuth',
                    'bearerAuth'
                ],
                'endpoint_path': '/groups/{type}/new',
                'operation_id': 'groups_type_new_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'type',
                    'inline_object',
                    'aid',
                ],
                'required': [
                    'type',
                    'inline_object',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'type':
                        (GroupType,),
                    'inline_object':
                        (InlineObject,),
                    'aid':
                        (int,),
                },
                'attribute_map': {
                    'type': 'type',
                    'aid': 'aid',
                },
                'location_map': {
                    'type': 'path',
                    'inline_object': 'body',
                    'aid': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def groups_get(
        self,
        **kwargs
    ):
        """Returns a list of all labels (formerly called groups) configured in ThousandEyes.  # noqa: E501

        This includes both Agent and Test labels.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            aid (int): Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            InlineResponse2008
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.groups_get_endpoint.call_with_http_info(**kwargs)

    def groups_group_id_delete_post(
        self,
        group_id,
        **kwargs
    ):
        """Deletes a label (formerly called group) currently configured in ThousandEyes.  # noqa: E501

        Note that built-in labels (with negative groupId numbers) are not eligible for deletion.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_group_id_delete_post(group_id, async_req=True)
        >>> result = thread.get()

        Args:
            group_id (int): the label that you wish to delete, found in either the `/groups` or the `/groups/{type}` endpoint.

        Keyword Args:
            aid (int): Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['group_id'] = \
            group_id
        return self.groups_group_id_delete_post_endpoint.call_with_http_info(**kwargs)

    def groups_group_id_get(
        self,
        group_id,
        **kwargs
    ):
        """Returns details for a label (formerly called group) configured in ThousandEyes.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_group_id_get(group_id, async_req=True)
        >>> result = thread.get()

        Args:
            group_id (int): the ID of the label to retrieve

        Keyword Args:
            aid (int): Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            InlineResponse2009
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['group_id'] = \
            group_id
        return self.groups_group_id_get_endpoint.call_with_http_info(**kwargs)

    def groups_group_id_update_post(
        self,
        group_id,
        inline_object1,
        **kwargs
    ):
        """Updates a label (formerly called group) in ThousandEyes, based on properties provided in the POST data.  # noqa: E501

        In order to edit a label, the user must have access to the target label, and have access to modify the objects that the label contains. For example, to update an agent label, the user needs the Edit Agents permission assigned to their role.<br><br> Regular users are blocked from using any of the POST-based methods.<br><br> Note: When creating or updating a label and assigning agents or tests, the user needs permission to modify the objects being added.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_group_id_update_post(group_id, inline_object1, async_req=True)
        >>> result = thread.get()

        Args:
            group_id (int): the label that you wish to update, found in either the `/groups` or the `/groups/{type}` endpoint.
            inline_object1 (InlineObject1):

        Keyword Args:
            aid (int): Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            InlineResponse201
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['group_id'] = \
            group_id
        kwargs['inline_object1'] = \
            inline_object1
        return self.groups_group_id_update_post_endpoint.call_with_http_info(**kwargs)

    def groups_type_get(
        self,
        type,
        **kwargs
    ):
        """Returns a list of all tests of the label (formerly called group) type specified, configured in ThousandEyes.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_type_get(type, async_req=True)
        >>> result = thread.get()

        Args:
            type (GroupType):

        Keyword Args:
            aid (int): Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            InlineResponse2008
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['type'] = \
            type
        return self.groups_type_get_endpoint.call_with_http_info(**kwargs)

    def groups_type_group_id_get(
        self,
        type,
        group_id,
        **kwargs
    ):
        """Returns a list of all labels (formerly called groups) configured in ThousandEyes.  # noqa: E501

        This includes both Agent and Test labels.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_type_group_id_get(type, group_id, async_req=True)
        >>> result = thread.get()

        Args:
            type (GroupType):
            group_id (int): the ID of the label to retrieve

        Keyword Args:
            aid (int): Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            InlineResponse2009
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['type'] = \
            type
        kwargs['group_id'] = \
            group_id
        return self.groups_type_group_id_get_endpoint.call_with_http_info(**kwargs)

    def groups_type_new_post(
        self,
        type,
        inline_object,
        **kwargs
    ):
        """Creates a new label (formerly called group) in ThousandEyes, based on properties provided in the POST data.  # noqa: E501

        In order to create a new label, the user attempting the creation must have sufficient privileges to create labels.<br><br> Regular users are blocked from using any of the POST-based methods.<br><br> Note: When creating or updating a label and assigning agents or tests, the user needs permission to modify the objects being added.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.groups_type_new_post(type, inline_object, async_req=True)
        >>> result = thread.get()

        Args:
            type (GroupType):
            inline_object (InlineObject):

        Keyword Args:
            aid (int): Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            InlineResponse201
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['type'] = \
            type
        kwargs['inline_object'] = \
            inline_object
        return self.groups_type_new_post_endpoint.call_with_http_info(**kwargs)

