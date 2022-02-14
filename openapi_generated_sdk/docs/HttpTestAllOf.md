# HttpTestAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** | HTTP Authentication type; defaults to NONE | [optional] 
**client_certificate** | **str** | String representation (containing newline characters) of client certificate, if used | [optional] 
**content_regex** | **str** | This field does not require escaping | [optional] 
**desired_status_code** | **str** | Set to the value you’re interested in retrieving. | [optional] 
**download_limit** | **int** | specify maximum number of bytes to download from the target object | [optional] 
**dns_override** | **str** | IP address to use for DNS override | [optional] 
**follow_redirects** | **bool** | set to 0 to not follow HTTP/301 or HTTP/302 redirect directives. Default is 1 | [optional] 
**headers** | **[str]** | array of header strings &#x60;[\&quot;header: value\&quot;, \&quot;header2: value\&quot;]&#x60;; use HTTP header values in this list | [optional] 
**http_version** | **int** | 2 for default (prefer HTTP/2), 1 for HTTP/1.1 only | [optional] 
**http_target_time** | **int** | target time for HTTP server completion; specified in milliseconds | [optional] 
**http_time_limit** | **int** | defaults to 5 seconds | [optional] 
**password** | **str** | password to be used for Basic/NTLM authentication | [optional] 
**post_body** | **str** | Enter the post body in this field. No escaping is required. If the post body is set to something other than empty, the requestMethod will be set to POST. | [optional] 
**ssl_version** | **str** | Read Only; corresponds to sslVersionId; Reflects the verbose ssl protocol version used by a test | [optional] 
**ssl_version_id** | **int** | 0 for auto, 3 for SSLv3, 4 for TLS v1.0, 5 for TLS v1.1, 6 for TLS v1.2 | [optional] 
**url** | **str** | target for the test | [optional] 
**use_ntlm** | **bool** | choose 1 to use NTLM, 0 to use Basic Authentication. Requires username/password to be set | [optional] 
**user_agent** | **str** | user-agent string to be provided during the test | [optional] 
**username** | **str** | username to be used for Basic/NTLM authentication | [optional] 
**verify_certificate** | **bool** | set to 0 to ignore certificate errors (defaults to 1) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


