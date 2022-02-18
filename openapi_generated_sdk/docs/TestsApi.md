# openapi_client.TestsApi

All URIs are relative to *https://api.thousandeyes.com/v6*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tests_get**](TestsApi.md#tests_get) | **GET** /tests | Returns a list of all tests configured in ThousandEyes.
[**tests_test_id_get**](TestsApi.md#tests_test_id_get) | **GET** /tests/{testId} | Returns a details for a test, including test type, name, intervals, targets, alert rules and agents.
[**tests_test_type_get**](TestsApi.md#tests_test_type_get) | **GET** /tests/{testType} | Returns a list of all tests of the type specified, configured in ThousandEyes.
[**tests_test_type_new_post**](TestsApi.md#tests_test_type_new_post) | **POST** /tests/{testType}/new | Creates a new test in ThousandEyes, based on properties provided in the POST data.
[**tests_test_type_test_id_delete_post**](TestsApi.md#tests_test_type_test_id_delete_post) | **POST** /tests/{testType}/{testId}/delete | Deletes the specified test in ThousandEyes, based on the testId provided in the API request.
[**tests_test_type_test_id_update_post**](TestsApi.md#tests_test_type_test_id_update_post) | **POST** /tests/{testType}/{testId}/update | Updates a test in ThousandEyes, based on properties provided in the POST data.


# **tests_get**
> InlineResponse2001 tests_get()

Returns a list of all tests configured in ThousandEyes.

Also returns data for saved events, which are indicated by a boolean field, `\"savedEvent\": 1`

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import tests_api
from openapi_client.model.inline_response2001 import InlineResponse2001
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
    api_instance = tests_api.TestsApi(api_client)
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of all tests configured in ThousandEyes.
        api_response = api_instance.tests_get(aid=aid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TestsApi->tests_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sends back an array of tests. |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tests_test_id_get**
> InlineResponse2001 tests_test_id_get(test_id)

Returns a details for a test, including test type, name, intervals, targets, alert rules and agents.

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import tests_api
from openapi_client.model.inline_response2001 import InlineResponse2001
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
    api_instance = tests_api.TestsApi(api_client)
    test_id = 1 # int | the ID of the test you wish to retrieve
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a details for a test, including test type, name, intervals, targets, alert rules and agents.
        api_response = api_instance.tests_test_id_get(test_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TestsApi->tests_test_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a details for a test, including test type, name, intervals, targets, alert rules and agents.
        api_response = api_instance.tests_test_id_get(test_id, aid=aid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TestsApi->tests_test_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **int**| the ID of the test you wish to retrieve |
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sends back an array of tests. |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tests_test_type_get**
> InlineResponse2001 tests_test_type_get(test_type)

Returns a list of all tests of the type specified, configured in ThousandEyes.

Also returns data for saved events, which are indicated by a boolean field, `\"savedEvent\": 1`

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import tests_api
from openapi_client.model.inline_response2001 import InlineResponse2001
from openapi_client.model.test_type import TestType
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
    api_instance = tests_api.TestsApi(api_client)
    test_type = TestType("agent-to-server") # TestType | 
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of all tests of the type specified, configured in ThousandEyes.
        api_response = api_instance.tests_test_type_get(test_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TestsApi->tests_test_type_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of all tests of the type specified, configured in ThousandEyes.
        api_response = api_instance.tests_test_type_get(test_type, aid=aid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TestsApi->tests_test_type_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_type** | **TestType**|  |
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sends back an array of tests. |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tests_test_type_new_post**
> InlineResponse2001 tests_test_type_new_post(test_type, workaround_agent_to_server_test)

Creates a new test in ThousandEyes, based on properties provided in the POST data.

In order to create a new test, the user attempting the creation must be an Account Admin.<br><br> Regular users are blocked from using any of the POST-based methods.<br><br> Note: When creating or updating a test and assigning alert rules, that alert rules are based on specific measurements being available. For example, when creating an HTTP server test with network measurements disabled, you will not be able to assign any alert rules that are based on network metrics. The same applies to BGP measurements. 

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import tests_api
from openapi_client.model.inline_response2001 import InlineResponse2001
from openapi_client.model.test_type import TestType
from openapi_client.model.workaround_agent_to_server_test import WorkaroundAgentToServerTest
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
    api_instance = tests_api.TestsApi(api_client)
    test_type = TestType("agent-to-server") # TestType | 
    workaround_agent_to_server_test = WorkaroundAgentToServerTest(None) # WorkaroundAgentToServerTest | Request body should contain fields to be set during creation.
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates a new test in ThousandEyes, based on properties provided in the POST data.
        api_response = api_instance.tests_test_type_new_post(test_type, workaround_agent_to_server_test)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TestsApi->tests_test_type_new_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a new test in ThousandEyes, based on properties provided in the POST data.
        api_response = api_instance.tests_test_type_new_post(test_type, workaround_agent_to_server_test, aid=aid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TestsApi->tests_test_type_new_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_type** | **TestType**|  |
 **workaround_agent_to_server_test** | [**WorkaroundAgentToServerTest**](WorkaroundAgentToServerTest.md)| Request body should contain fields to be set during creation. |
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the test definition |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tests_test_type_test_id_delete_post**
> tests_test_type_test_id_delete_post(test_type, test_id)

Deletes the specified test in ThousandEyes, based on the testId provided in the API request.

In order to delete a test, the user attempting the creation must be an Account Admin.<br><br> Regular users are blocked from using any of the POST-based methods. 

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import tests_api
from openapi_client.model.test_type import TestType
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
    api_instance = tests_api.TestsApi(api_client)
    test_type = TestType("agent-to-server") # TestType | 
    test_id = 1 # int | corresponds to a testId of the type specified by `{testType}`, see the test list endpoint for a listing of tests
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletes the specified test in ThousandEyes, based on the testId provided in the API request.
        api_instance.tests_test_type_test_id_delete_post(test_type, test_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TestsApi->tests_test_type_test_id_delete_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes the specified test in ThousandEyes, based on the testId provided in the API request.
        api_instance.tests_test_type_test_id_delete_post(test_type, test_id, aid=aid)
    except openapi_client.ApiException as e:
        print("Exception when calling TestsApi->tests_test_type_test_id_delete_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_type** | **TestType**|  |
 **test_id** | **int**| corresponds to a testId of the type specified by &#x60;{testType}&#x60;, see the test list endpoint for a listing of tests |
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
**204** | If a test is successfully deleted, an HTTP/204 NO CONTENT response will be returned, and an empty JSON response will be in the body of the response. |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tests_test_type_test_id_update_post**
> InlineResponse2001 tests_test_type_test_id_update_post(test_type, test_id, workaround_agent_to_server_test)

Updates a test in ThousandEyes, based on properties provided in the POST data.

In order to edit a test, the user attempting the creation must be an Account Admin, and the target test cannot be a live share or saved event.<br><br> Regular users are blocked from using any of the POST-based methods.<br><br> Note: When creating or updating a test and assigning alert rules, that alert rules are based on specific measurements being available. For example, when creating an HTTP server test with network measurements disabled, you will not be able to assign any alert rules that are based on network metrics. The same applies to BGP measurements. 

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import tests_api
from openapi_client.model.inline_response2001 import InlineResponse2001
from openapi_client.model.test_type import TestType
from openapi_client.model.workaround_agent_to_server_test import WorkaroundAgentToServerTest
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
    api_instance = tests_api.TestsApi(api_client)
    test_type = TestType("agent-to-server") # TestType | 
    test_id = 1 # int | corresponds to a testId of the type specified by `{testType}`, see the test list endpoint for a listing of tests
    workaround_agent_to_server_test = WorkaroundAgentToServerTest(None) # WorkaroundAgentToServerTest | Request body should contain fields to be set during creation.
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates a test in ThousandEyes, based on properties provided in the POST data.
        api_response = api_instance.tests_test_type_test_id_update_post(test_type, test_id, workaround_agent_to_server_test)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TestsApi->tests_test_type_test_id_update_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a test in ThousandEyes, based on properties provided in the POST data.
        api_response = api_instance.tests_test_type_test_id_update_post(test_type, test_id, workaround_agent_to_server_test, aid=aid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TestsApi->tests_test_type_test_id_update_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_type** | **TestType**|  |
 **test_id** | **int**| corresponds to a testId of the type specified by &#x60;{testType}&#x60;, see the test list endpoint for a listing of tests |
 **workaround_agent_to_server_test** | [**WorkaroundAgentToServerTest**](WorkaroundAgentToServerTest.md)| Request body should contain fields to be set during creation. |
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If a test is successfully edited, an HTTP/200 OK response will be returned, and the test definition will be returned. The modifiedBy and modifiedDate fields should be updated according to the user who edited the account |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

