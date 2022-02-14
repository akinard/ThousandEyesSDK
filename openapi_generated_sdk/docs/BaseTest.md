# BaseTest


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
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


