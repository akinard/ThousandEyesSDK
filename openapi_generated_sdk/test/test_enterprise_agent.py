"""
    Thousand Eyes API V6

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 6.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.agent_type import AgentType
from openapi_client.model.cloud_agent import CloudAgent
from openapi_client.model.enterprise_agent_all_of import EnterpriseAgentAllOf
from openapi_client.model.enterprise_agent_all_of_error_details import EnterpriseAgentAllOfErrorDetails
from openapi_client.model.group import Group
globals()['AgentType'] = AgentType
globals()['CloudAgent'] = CloudAgent
globals()['EnterpriseAgentAllOf'] = EnterpriseAgentAllOf
globals()['EnterpriseAgentAllOfErrorDetails'] = EnterpriseAgentAllOfErrorDetails
globals()['Group'] = Group
from openapi_client.model.enterprise_agent import EnterpriseAgent


class TestEnterpriseAgent(unittest.TestCase):
    """EnterpriseAgent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEnterpriseAgent(self):
        """Test EnterpriseAgent"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EnterpriseAgent()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()