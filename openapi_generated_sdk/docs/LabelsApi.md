# openapi_client.LabelsApi

All URIs are relative to *https://api.thousandeyes.com/v6*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_get**](LabelsApi.md#groups_get) | **GET** /groups | Returns a list of all labels (formerly called groups) configured in ThousandEyes.
[**groups_group_id_delete_post**](LabelsApi.md#groups_group_id_delete_post) | **POST** /groups/{groupId}/delete | Deletes a label (formerly called group) currently configured in ThousandEyes.
[**groups_group_id_get**](LabelsApi.md#groups_group_id_get) | **GET** /groups/{groupId} | Returns details for a label (formerly called group) configured in ThousandEyes.
[**groups_group_id_update_post**](LabelsApi.md#groups_group_id_update_post) | **POST** /groups/{groupId}/update | Updates a label (formerly called group) in ThousandEyes, based on properties provided in the POST data.
[**groups_type_get**](LabelsApi.md#groups_type_get) | **GET** /groups/{type} | Returns a list of all tests of the label (formerly called group) type specified, configured in ThousandEyes.
[**groups_type_group_id_get**](LabelsApi.md#groups_type_group_id_get) | **GET** /groups/{type}/{groupId} | Returns a list of all labels (formerly called groups) configured in ThousandEyes.
[**groups_type_new_post**](LabelsApi.md#groups_type_new_post) | **POST** /groups/{type}/new | Creates a new label (formerly called group) in ThousandEyes, based on properties provided in the POST data.


# **groups_get**
> InlineResponse2008 groups_get()

Returns a list of all labels (formerly called groups) configured in ThousandEyes.

This includes both Agent and Test labels.

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import labels_api
from openapi_client.model.inline_response2008 import InlineResponse2008
from pprint import pprint
# Defining the host is optional and defaults to https://api.thousandeyes.com/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.thousandeyes.com/v6"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (token): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = labels_api.LabelsApi(api_client)
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of all labels (formerly called groups) configured in ThousandEyes.
        api_response = api_instance.groups_get(aid=aid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LabelsApi->groups_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sends back an array of labels configured in the platform. |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_id_delete_post**
> groups_group_id_delete_post(group_id)

Deletes a label (formerly called group) currently configured in ThousandEyes.

Note that built-in labels (with negative groupId numbers) are not eligible for deletion. 

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import labels_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.thousandeyes.com/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.thousandeyes.com/v6"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (token): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = labels_api.LabelsApi(api_client)
    group_id = 1 # int | the label that you wish to delete, found in either the `/groups` or the `/groups/{type}` endpoint.
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletes a label (formerly called group) currently configured in ThousandEyes.
        api_instance.groups_group_id_delete_post(group_id)
    except openapi_client.ApiException as e:
        print("Exception when calling LabelsApi->groups_group_id_delete_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes a label (formerly called group) currently configured in ThousandEyes.
        api_instance.groups_group_id_delete_post(group_id, aid=aid)
    except openapi_client.ApiException as e:
        print("Exception when calling LabelsApi->groups_group_id_delete_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| the label that you wish to delete, found in either the &#x60;/groups&#x60; or the &#x60;/groups/{type}&#x60; endpoint. |
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | If a label is successfully deleted, an HTTP/204 NO CONTENT response will be returned, and an empty JSON response will be in the body of the response. |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_id_get**
> InlineResponse2009 groups_group_id_get(group_id)

Returns details for a label (formerly called group) configured in ThousandEyes.

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import labels_api
from openapi_client.model.inline_response2009 import InlineResponse2009
from pprint import pprint
# Defining the host is optional and defaults to https://api.thousandeyes.com/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.thousandeyes.com/v6"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (token): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = labels_api.LabelsApi(api_client)
    group_id = 1 # int | the ID of the label to retrieve
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns details for a label (formerly called group) configured in ThousandEyes.
        api_response = api_instance.groups_group_id_get(group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LabelsApi->groups_group_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns details for a label (formerly called group) configured in ThousandEyes.
        api_response = api_instance.groups_group_id_get(group_id, aid=aid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LabelsApi->groups_group_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| the ID of the label to retrieve |
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sends back an array of labels configured in the platform. |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_group_id_update_post**
> InlineResponse201 groups_group_id_update_post(group_id, inline_object1)

Updates a label (formerly called group) in ThousandEyes, based on properties provided in the POST data.

In order to edit a label, the user must have access to the target label, and have access to modify the objects that the label contains. For example, to update an agent label, the user needs the Edit Agents permission assigned to their role.<br><br> Regular users are blocked from using any of the POST-based methods.<br><br> Note: When creating or updating a label and assigning agents or tests, the user needs permission to modify the objects being added. 

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import labels_api
from openapi_client.model.inline_response201 import InlineResponse201
from openapi_client.model.inline_object1 import InlineObject1
from pprint import pprint
# Defining the host is optional and defaults to https://api.thousandeyes.com/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.thousandeyes.com/v6"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (token): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = labels_api.LabelsApi(api_client)
    group_id = 1 # int | the label that you wish to update, found in either the `/groups` or the `/groups/{type}` endpoint.
    inline_object1 = InlineObject1(
        name="name_example",
        tests=[
            GroupsTypeNewTests(
                test_id=1,
            ),
        ],
        agents=[
            GroupsTypeNewAgents(
                agent_id=1,
            ),
        ],
    ) # InlineObject1 | 
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates a label (formerly called group) in ThousandEyes, based on properties provided in the POST data.
        api_response = api_instance.groups_group_id_update_post(group_id, inline_object1)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LabelsApi->groups_group_id_update_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a label (formerly called group) in ThousandEyes, based on properties provided in the POST data.
        api_response = api_instance.groups_group_id_update_post(group_id, inline_object1, aid=aid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LabelsApi->groups_group_id_update_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| the label that you wish to update, found in either the &#x60;/groups&#x60; or the &#x60;/groups/{type}&#x60; endpoint. |
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  |
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the label definition |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_type_get**
> InlineResponse2008 groups_type_get(type)

Returns a list of all tests of the label (formerly called group) type specified, configured in ThousandEyes.

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import labels_api
from openapi_client.model.group_type import GroupType
from openapi_client.model.inline_response2008 import InlineResponse2008
from pprint import pprint
# Defining the host is optional and defaults to https://api.thousandeyes.com/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.thousandeyes.com/v6"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (token): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = labels_api.LabelsApi(api_client)
    type = GroupType("tests") # GroupType | 
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of all tests of the label (formerly called group) type specified, configured in ThousandEyes.
        api_response = api_instance.groups_type_get(type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LabelsApi->groups_type_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of all tests of the label (formerly called group) type specified, configured in ThousandEyes.
        api_response = api_instance.groups_type_get(type, aid=aid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LabelsApi->groups_type_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **GroupType**|  |
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sends back an array of labels configured in the platform. |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_type_group_id_get**
> InlineResponse2009 groups_type_group_id_get(type, group_id)

Returns a list of all labels (formerly called groups) configured in ThousandEyes.

This includes both Agent and Test labels.

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import labels_api
from openapi_client.model.group_type import GroupType
from openapi_client.model.inline_response2009 import InlineResponse2009
from pprint import pprint
# Defining the host is optional and defaults to https://api.thousandeyes.com/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.thousandeyes.com/v6"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (token): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = labels_api.LabelsApi(api_client)
    type = GroupType("tests") # GroupType | 
    group_id = 1 # int | the ID of the label to retrieve
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of all labels (formerly called groups) configured in ThousandEyes.
        api_response = api_instance.groups_type_group_id_get(type, group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LabelsApi->groups_type_group_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of all labels (formerly called groups) configured in ThousandEyes.
        api_response = api_instance.groups_type_group_id_get(type, group_id, aid=aid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LabelsApi->groups_type_group_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **GroupType**|  |
 **group_id** | **int**| the ID of the label to retrieve |
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sends back an array of labels configured in the platform. |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_type_new_post**
> InlineResponse201 groups_type_new_post(type, inline_object)

Creates a new label (formerly called group) in ThousandEyes, based on properties provided in the POST data.

In order to create a new label, the user attempting the creation must have sufficient privileges to create labels.<br><br> Regular users are blocked from using any of the POST-based methods.<br><br> Note: When creating or updating a label and assigning agents or tests, the user needs permission to modify the objects being added. 

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import labels_api
from openapi_client.model.group_type import GroupType
from openapi_client.model.inline_object import InlineObject
from openapi_client.model.inline_response201 import InlineResponse201
from pprint import pprint
# Defining the host is optional and defaults to https://api.thousandeyes.com/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.thousandeyes.com/v6"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (token): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = labels_api.LabelsApi(api_client)
    type = GroupType("tests") # GroupType | 
    inline_object = InlineObject(
        name="name_example",
        tests=[
            GroupsTypeNewTests(
                test_id=1,
            ),
        ],
        agents=[
            GroupsTypeNewAgents(
                agent_id=1,
            ),
        ],
    ) # InlineObject | 
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates a new label (formerly called group) in ThousandEyes, based on properties provided in the POST data.
        api_response = api_instance.groups_type_new_post(type, inline_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LabelsApi->groups_type_new_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a new label (formerly called group) in ThousandEyes, based on properties provided in the POST data.
        api_response = api_instance.groups_type_new_post(type, inline_object, aid=aid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LabelsApi->groups_type_new_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **GroupType**|  |
 **inline_object** | [**InlineObject**](InlineObject.md)|  |
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the label definition |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

