# EnterpriseAgent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **int** | unique ID of agent | [optional] 
**agent_name** | **str** | display name of the agent | [optional] 
**agent_type** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**country_id** | **str** | ISO-3166-1 alpha-2 country code of the agent | [optional] 
**ip_addresses** | **[str]** | array of ipAddress entries | [optional] 
**location** | **str** | location of the agent | [optional] 
**groups** | [**[Group]**](Group.md) |  | [optional] 
**hostname** | **str** | fully qualified domain name of the agent | [optional] 
**prefix** | **str** | Network prefix, expressed in CIDR format | [optional] 
**enabled** | **bool** | 1 for enabled, 0 for disabled | [optional] 
**network** | **str** | name of the autonomous system in which the Agent is found | [optional] 
**created_date** | **datetime** | yyyy-MM-dd hh:mm:ss, expressed in UTC | [optional] 
**last_seen** | **datetime** | yyyy-MM-dd hh:mm:ss, expressed in UTC | [optional] 
**agent_state** | **str** |  | [optional] 
**verify_ssl_certificates** | **bool** | 1 for enabled, 0 for disabled | [optional] 
**keep_browser_cache** | **bool** | 1 for enabled, 0 for disabled | [optional] 
**utilization** | **int** | shows overall utilization percentage | [optional] 
**ipv6_policy** | **str** | IP version policy | [optional] 
**target_for_tests** | **str** | target IP address or domain name representing test destination when agent is acting as a test target in an agent-to-agent test | [optional] 
**public_ip_addresses** | **[str]** | array of ipAddress entries | [optional] 
**error_details** | [**EnterpriseAgentAllOfErrorDetails**](EnterpriseAgentAllOfErrorDetails.md) |  | [optional] 
**account_groups** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** | list of account groups to which the agent is assigned, showing aid and accountGroupName fields | [optional] 
**notification_rules** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** | array of notification rule objects configured on agent | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


