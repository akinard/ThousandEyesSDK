"""
    Thousand Eyes API V6

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 6.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.tests_api import TestsApi  # noqa: E501


class TestTestsApi(unittest.TestCase):
    """TestsApi unit test stubs"""

    def setUp(self):
        self.api = TestsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_tests_get(self):
        """Test case for tests_get

        Returns a list of all tests configured in ThousandEyes.  # noqa: E501
        """
        pass

    def test_tests_test_id_get(self):
        """Test case for tests_test_id_get

        Returns a details for a test, including test type, name, intervals, targets, alert rules and agents.  # noqa: E501
        """
        pass

    def test_tests_test_type_get(self):
        """Test case for tests_test_type_get

        Returns a list of all tests of the type specified, configured in ThousandEyes.  # noqa: E501
        """
        pass

    def test_tests_test_type_new_post(self):
        """Test case for tests_test_type_new_post

        Creates a new test in ThousandEyes, based on properties provided in the POST data.  # noqa: E501
        """
        pass

    def test_tests_test_type_test_id_delete_post(self):
        """Test case for tests_test_type_test_id_delete_post

        Deletes the specified test in ThousandEyes, based on the testId provided in the API request.  # noqa: E501
        """
        pass

    def test_tests_test_type_test_id_update_post(self):
        """Test case for tests_test_type_test_id_update_post

        Updates a test in ThousandEyes, based on properties provided in the POST data.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
