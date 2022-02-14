# ServerTest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts_enabled** | **bool** | choose 1 to enable alerts, or 0 to disable alerts. Defaults to 1 | [optional] 
**alert_rules** | [**[BaseTestAlertRules]**](BaseTestAlertRules.md) | array of alert rule objects &#x60;{\&quot;ruleId\&quot;: ruleId}&#x60;; get ruleId from &#x60;/alert-rules&#x60; endpoint. If alertsEnabled is set to 1 and alertRules is not included in a creation/update query, applicable defaults will be used. | [optional] 
**api_links** | [**[BaseTestApiLinks]**](BaseTestApiLinks.md) | array of apiLinks objects, showing rel and href elements; Read only; self links to endpoint to pull test metadata, and data links to endpoint for test data | [optional] 
**created_by** | **str** | Username (email@company.com); read only | [optional] 
**created_date** | **datetime** | YYYY-MM-DD HH:mm:ss formatted date; read only; shown in UTC | [optional] 
**description** | **str** | defaults to empty string | [optional] 
**enabled** | **bool** | choose 1 to enable the test, 0 to disable the test | [optional] 
**groups** | [**[Group]**](Group.md) | array of label objects (&#x60;\&quot;groups\&quot;: [ { \&quot;name\&quot;: \&quot;groupName\&quot;, \&quot;groupId\&quot;: groupId, \&quot;builtIn\&quot;: 0}]&#x60;); get groupId from /groupsendpoint. | [optional] 
**modified_by** | **str** | Username (email@company.com); read only | [optional] 
**modified_date** | **datetime** | YYYY-MM-DD HH:mm:ss formatted date; read only; shown in UTC | [optional] 
**saved_event** | **bool** | read only; indicates 1 for a saved event, 0 for a normal test | [optional] 
**shared_with_accounts** | [**[BaseTestSharedWithAccounts]**](BaseTestSharedWithAccounts.md) | array of account group objects (&#x60;\&quot;sharedWithAccounts\&quot;: [{\&quot;aid\&quot;: aid, \&quot;name\&quot;: \&quot;AccountGroupName\&quot;}]&#x60;); Test is shared with the listed accout groups. Get aid and name from account-groups endpoint. | [optional] 
**test_id** | **int** | unique ID of test; read only; each test is assigned a unique ID; this is used to access test data from other endpoints. | [optional] 
**test_name** | **str** | Test name must be unique | [optional] 
**type** | [**TestType**](TestType.md) |  | [optional] 
**live_share** | **bool** | read only; indicates 1 for a test shared with your account group, 0 for a normal test | [optional] 
**agents** | [**[ServerTestAllOfAgents]**](ServerTestAllOfAgents.md) | array of agent objects &#x60;{\&quot;agentId\&quot;: agentId}&#x60;; get agentId from /agents endpoint. | [optional] 
**bandwidth_measurements** | **bool** | set to 1 to measure bandwidth. Only applies to Enterprise Agents assigned to the test, and requires that networkMeasurements is set. | [optional] 
**bgp_measurements** | **bool** | choose 1 to enable bgp measurements, 0 to disable; defaults to 1 when networkMeasurements is set | [optional] 
**bgp_monitors** | [**[ServerTestAllOfBgpMonitors]**](ServerTestAllOfBgpMonitors.md) | array of BGP Monitor objects &#x60;{\&quot;monitorId\&quot;: monitorId}&#x60;; get monitorId from /bgp-monitors endpoint. | [optional] 
**interval** | [**TestInterval**](TestInterval.md) |  | [optional] 
**mtu_measurements** | **bool** | set to 1 to measure MTU sizes on network from agents to the target | [optional] 
**network_measurements** | **bool** | choose 1 to enable network measurements, 0 to disable; defaults to 1 | [optional] 
**num_path_traces** | **int** | defaults to 3 | [optional] 
**path_trace_mode** | **str** | choose &#x60;inSession&#x60; to perform the path trace within a TCP session; defaults to &#x60;classic&#x60; | [optional] 
**probe_mode** | **str** | probe mode used by End-to-end Network Test; only valid if &#x60;protocol&#x60; is set to &#x60;TCP&#x60;; defaults to &#x60;AUTO&#x60; | [optional] 
**protocol** | **str** | protocol used by dependent Network tests (End-to-end, Path Trace, PMTUD); defaults to &#x60;TCP&#x60; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


