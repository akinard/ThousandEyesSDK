# openapi_client.AgentsMonitorsApi

All URIs are relative to *https://api.thousandeyes.com/v6*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agents_agent_id_get**](AgentsMonitorsApi.md#agents_agent_id_get) | **GET** /agents/{agentId} | Returns details for an agent, including assigned tests.
[**agents_get**](AgentsMonitorsApi.md#agents_get) | **GET** /agents | Returns a list of all agents available to your account in ThousandEyes, including both Enterprise and Cloud agents.


# **agents_agent_id_get**
> InlineResponse2002 agents_agent_id_get(agent_id)

Returns details for an agent, including assigned tests.

Enterprise agents show utilization data and assigned accounts.

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import agents__monitors_api
from openapi_client.model.inline_response2002 import InlineResponse2002
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
    api_instance = agents__monitors_api.AgentsMonitorsApi(api_client)
    agent_id = 1 # int | the ID of the label to retrieve
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns details for an agent, including assigned tests.
        api_response = api_instance.agents_agent_id_get(agent_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AgentsMonitorsApi->agents_agent_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns details for an agent, including assigned tests.
        api_response = api_instance.agents_agent_id_get(agent_id, aid=aid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AgentsMonitorsApi->agents_agent_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **int**| the ID of the label to retrieve |
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

# **agents_get**
> InlineResponse2002 agents_get()

Returns a list of all agents available to your account in ThousandEyes, including both Enterprise and Cloud agents.

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import agents__monitors_api
from openapi_client.model.agent_type import AgentType
from openapi_client.model.inline_response2002 import InlineResponse2002
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
    api_instance = agents__monitors_api.AgentsMonitorsApi(api_client)
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)
    agent_types = AgentType([
        "CLOUD",
    ]) # AgentType | Specifies the type of agents requested. Accepts either a single allowed value or a comma-separated list of allowed values (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of all agents available to your account in ThousandEyes, including both Enterprise and Cloud agents.
        api_response = api_instance.agents_get(aid=aid, agent_types=agent_types)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AgentsMonitorsApi->agents_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]
 **agent_types** | **AgentType**| Specifies the type of agents requested. Accepts either a single allowed value or a comma-separated list of allowed values | [optional]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

