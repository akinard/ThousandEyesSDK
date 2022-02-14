# openapi_client.AlertsNotificationsApi

All URIs are relative to *https://api.thousandeyes.com/v6*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alert_rules_get**](AlertsNotificationsApi.md#alert_rules_get) | **GET** /alert-rules | Returns a list of all alert rules configured under your account in ThousandEyes.
[**alert_rules_new_post**](AlertsNotificationsApi.md#alert_rules_new_post) | **POST** /alert-rules/new | Creates a new alert rule in your account, based on properties provided in the POST data.
[**alert_rules_rule_id_delete_post**](AlertsNotificationsApi.md#alert_rules_rule_id_delete_post) | **POST** /alert-rules/{ruleId}/delete | Deletes an alert rule in your account.
[**alert_rules_rule_id_get**](AlertsNotificationsApi.md#alert_rules_rule_id_get) | **GET** /alert-rules/{ruleId} | Returns details about an alert rule.
[**alert_rules_rule_id_update_post**](AlertsNotificationsApi.md#alert_rules_rule_id_update_post) | **POST** /alert-rules/{ruleId}/update | Modifies an existing alert rule in your account, based on properties provided in the POST data.
[**alerts_alert_id_get**](AlertsNotificationsApi.md#alerts_alert_id_get) | **GET** /alerts/{alertId} | Returns details about an alert.
[**alerts_get**](AlertsNotificationsApi.md#alerts_get) | **GET** /alerts | Returns a list of all active alerts, active at any given time.
[**integrations_get**](AlertsNotificationsApi.md#integrations_get) | **GET** /integrations | Returns a list of all alert notification integrations (webhooks, PagerDuty, Slack, …)


# **alert_rules_get**
> InlineResponse2005 alert_rules_get()

Returns a list of all alert rules configured under your account in ThousandEyes.

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import alerts__notifications_api
from openapi_client.model.inline_response2005 import InlineResponse2005
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
    api_instance = alerts__notifications_api.AlertsNotificationsApi(api_client)
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of all alert rules configured under your account in ThousandEyes.
        api_response = api_instance.alert_rules_get(aid=aid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsNotificationsApi->alert_rules_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sends back an array of alert rules, indicating ruleID, whether or not the alert is enabled, recipient lists, and the rule criteria and clearing logic. Default rules for each type are indicated with a bit response (1 or 0); default alert rules are assigned by default to each type of test to which they apply. |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_rules_new_post**
> InlineResponse2005 alert_rules_new_post(unknown_base_type)

Creates a new alert rule in your account, based on properties provided in the POST data.

In order to create a new alert rule, the user attempting the creation must be in a role that has the Edit alert rules permission. Users without this permission will receive an error.<br><br>Note: when assigning any alert rule to a test (which can be done as part of the creation activity), the user must be in a role that has the Edit tests permission.

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import alerts__notifications_api
from openapi_client.model.alert_rule import AlertRule
from openapi_client.model.unknownbasetype import UNKNOWNBASETYPE
from openapi_client.model.inline_response2005 import InlineResponse2005
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
    api_instance = alerts__notifications_api.AlertsNotificationsApi(api_client)
    unknown_base_type = None # UNKNOWN_BASE_TYPE | 
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates a new alert rule in your account, based on properties provided in the POST data.
        api_response = api_instance.alert_rules_new_post(unknown_base_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsNotificationsApi->alert_rules_new_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a new alert rule in your account, based on properties provided in the POST data.
        api_response = api_instance.alert_rules_new_post(unknown_base_type, aid=aid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsNotificationsApi->alert_rules_new_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | If successful, will respond with an HTTP/201 response and a body which contains the new alert rule definition. |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_rules_rule_id_delete_post**
> alert_rules_rule_id_delete_post(rule_id)

Deletes an alert rule in your account.

In order to delete an alert rule, the user attempting the creation must be in a role that has the Edit alert rules permission, as well as Edit Tests permission, in the event that the alert rule is assigned to any tests. Users without appropriate permissions will receive an error.

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import alerts__notifications_api
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
    api_instance = alerts__notifications_api.AlertsNotificationsApi(api_client)
    rule_id = 1 # int | the ID of the rule to delete
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletes an alert rule in your account.
        api_instance.alert_rules_rule_id_delete_post(rule_id)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsNotificationsApi->alert_rules_rule_id_delete_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes an alert rule in your account.
        api_instance.alert_rules_rule_id_delete_post(rule_id, aid=aid)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsNotificationsApi->alert_rules_rule_id_delete_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**| the ID of the rule to delete |
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
**204** | Response header will be returned as HTTP/204 response code. No response body will be returned. |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_rules_rule_id_get**
> InlineResponse2006 alert_rules_rule_id_get(rule_id)

Returns details about an alert rule.

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import alerts__notifications_api
from openapi_client.model.inline_response2006 import InlineResponse2006
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
    api_instance = alerts__notifications_api.AlertsNotificationsApi(api_client)
    rule_id = 1 # int | the ID of the rule to retrieve
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns details about an alert rule.
        api_response = api_instance.alert_rules_rule_id_get(rule_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsNotificationsApi->alert_rules_rule_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns details about an alert rule.
        api_response = api_instance.alert_rules_rule_id_get(rule_id, aid=aid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsNotificationsApi->alert_rules_rule_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**| the ID of the rule to retrieve |
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sends back detailed information about a specific alert rule. If the ruleId doesn’t exist or is inaccessible by your account, an empty response will be returned. |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_rules_rule_id_update_post**
> InlineResponse2005 alert_rules_rule_id_update_post(rule_id, unknown_base_type)

Modifies an existing alert rule in your account, based on properties provided in the POST data.

In order to modify an alert rule, the user attempting the creation must be in a role that has the Edit alert rules permission. Users without this permission will receive an error.<br><br>Note: when assigning any alert rule to a test (which can be done as part of the update activity), the user must be in a role that has the Edit tests permission.

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import alerts__notifications_api
from openapi_client.model.alert_rule import AlertRule
from openapi_client.model.unknownbasetype import UNKNOWNBASETYPE
from openapi_client.model.inline_response2005 import InlineResponse2005
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
    api_instance = alerts__notifications_api.AlertsNotificationsApi(api_client)
    rule_id = 1 # int | the ID of the rule to update
    unknown_base_type = None # UNKNOWN_BASE_TYPE | 
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Modifies an existing alert rule in your account, based on properties provided in the POST data.
        api_response = api_instance.alert_rules_rule_id_update_post(rule_id, unknown_base_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsNotificationsApi->alert_rules_rule_id_update_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Modifies an existing alert rule in your account, based on properties provided in the POST data.
        api_response = api_instance.alert_rules_rule_id_update_post(rule_id, unknown_base_type, aid=aid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsNotificationsApi->alert_rules_rule_id_update_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**| the ID of the rule to update |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If successful, will respond with an HTTP/200 response and the modified rule definition in the body. |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_alert_id_get**
> InlineResponse2004 alerts_alert_id_get(alert_id)

Returns details about an alert.

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import alerts__notifications_api
from openapi_client.model.inline_response2004 import InlineResponse2004
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
    api_instance = alerts__notifications_api.AlertsNotificationsApi(api_client)
    alert_id = 1 # int | the ID of the alert to retrieve
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns details about an alert.
        api_response = api_instance.alerts_alert_id_get(alert_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsNotificationsApi->alerts_alert_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns details about an alert.
        api_response = api_instance.alerts_alert_id_get(alert_id, aid=aid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsNotificationsApi->alerts_alert_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| the ID of the alert to retrieve |
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sends back detailed information about a specific alertId. If the alertId doesn’t exist or is inaccessible by your account, an empty response will be returned. |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_get**
> InlineResponse2003 alerts_get()

Returns a list of all active alerts, active at any given time.

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import alerts__notifications_api
from openapi_client.model.inline_response2003 import InlineResponse2003
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
    api_instance = alerts__notifications_api.AlertsNotificationsApi(api_client)
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)
    window = "4" # str | The window parameter is used to specify an amount of time in the past for which to fetch data. That is, data will be retrieved from the specified amount of time ago up until the time of the request. A time window is a number followed by an optional time interval type. The supported time interval types are s for seconds, m for minutes, h for hours, d for days, and w for weeks. If no time interval type is specified, seconds are assumed. For example, window=10d would retrieve data from the last 10 days, window=12h would retrieve data from the last 12 hours, and window=1200 will retrieve data from the last 1200 seconds. (optional)
    _from = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | `YYYY-mm-ddTHH:MM:SS` specifies an explicit start for your range of data. The to parameter is optional – if omitted, the current time (at the time of the request) will be assumed. Dates must be specified in the ISO 8601 date-time format, with hyphens between date fields and colons between time fields. The full time (hours, minutes, and seconds) must be included. The date and time can be separated by either a space or the letter T. Example: 2012-01-01T00:00:00. The date range is inclusive. Time zone is UTC. (optional)
    to = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | `YYYY-mm-ddTHH:MM:SS` specifies an explicit end for your range of data. The to parameter is optional – if omitted, the current time (at the time of the request) will be assumed. Dates must be specified in the ISO 8601 date-time format, with hyphens between date fields and colons between time fields. The full time (hours, minutes, and seconds) must be included. The date and time can be separated by either a space or the letter T. Example: 2012-01-01T00:00:00. The date range is inclusive. Time zone is UTC.<br><br>**Note** The `from`/`to` and `window` parameters are mutually exclusive – the server will produce a 400 error if both `window` and either `from` or `to` is specified. It will also produce a 400 error if `to` is specified without `from`. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of all active alerts, active at any given time.
        api_response = api_instance.alerts_get(aid=aid, window=window, _from=_from, to=to)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsNotificationsApi->alerts_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]
 **window** | **str**| The window parameter is used to specify an amount of time in the past for which to fetch data. That is, data will be retrieved from the specified amount of time ago up until the time of the request. A time window is a number followed by an optional time interval type. The supported time interval types are s for seconds, m for minutes, h for hours, d for days, and w for weeks. If no time interval type is specified, seconds are assumed. For example, window&#x3D;10d would retrieve data from the last 10 days, window&#x3D;12h would retrieve data from the last 12 hours, and window&#x3D;1200 will retrieve data from the last 1200 seconds. | [optional]
 **_from** | **datetime**| &#x60;YYYY-mm-ddTHH:MM:SS&#x60; specifies an explicit start for your range of data. The to parameter is optional – if omitted, the current time (at the time of the request) will be assumed. Dates must be specified in the ISO 8601 date-time format, with hyphens between date fields and colons between time fields. The full time (hours, minutes, and seconds) must be included. The date and time can be separated by either a space or the letter T. Example: 2012-01-01T00:00:00. The date range is inclusive. Time zone is UTC. | [optional]
 **to** | **datetime**| &#x60;YYYY-mm-ddTHH:MM:SS&#x60; specifies an explicit end for your range of data. The to parameter is optional – if omitted, the current time (at the time of the request) will be assumed. Dates must be specified in the ISO 8601 date-time format, with hyphens between date fields and colons between time fields. The full time (hours, minutes, and seconds) must be included. The date and time can be separated by either a space or the letter T. Example: 2012-01-01T00:00:00. The date range is inclusive. Time zone is UTC.&lt;br&gt;&lt;br&gt;**Note** The &#x60;from&#x60;/&#x60;to&#x60; and &#x60;window&#x60; parameters are mutually exclusive – the server will produce a 400 error if both &#x60;window&#x60; and either &#x60;from&#x60; or &#x60;to&#x60; is specified. It will also produce a 400 error if &#x60;to&#x60; is specified without &#x60;from&#x60;. | [optional]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sends back an array of active alerts, either at present, or based on the time range specified, indicating testId and testName, alert rule. If no alerts are active during the time range specified, an empty response will be returned. |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrations_get**
> InlineResponse2007 integrations_get()

Returns a list of all alert notification integrations (webhooks, PagerDuty, Slack, …)

### Example

* Basic Authentication (basicAuth):
* Bearer (token) Authentication (bearerAuth):

```python
import time
import openapi_client
from openapi_client.api import alerts__notifications_api
from openapi_client.model.inline_response2007 import InlineResponse2007
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
    api_instance = alerts__notifications_api.AlertsNotificationsApi(api_client)
    aid = 1 # int | Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of all alert notification integrations (webhooks, PagerDuty, Slack, …)
        api_response = api_instance.integrations_get(aid=aid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsNotificationsApi->integrations_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| Specifies the account group context of the request, obtained from the /account-groups endpoint. Specifying this parameter without the user being assigned to the target account will result in an error response. | [optional]

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an object with two array properties: thirdParty and webhook. |  * X-Organization-Rate-Limit-Limit -  <br>  * X-Organization-Rate-Limit-Remaining -  <br>  * X-Organization-Rate-Limit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

