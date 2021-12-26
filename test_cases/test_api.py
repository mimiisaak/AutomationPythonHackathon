
import pytest
from test_cases.conftest import my_mobile_starter
from workflows.api_flows import get_request, post_request, delete_request
from extensions import verifictions
@pytest.mark.usefixtures("init_api")
class Test_Api_Server:
    def test_01_get_post_list(self):
        response = get_request(self.url)
        post_list = response.text
        print(post_list)
        verifictions.verify_equals(response.status_code, 200)

    def test_02_create_post(self):
        payload = {'userId': '105', 'id': '', 'title': 'My Title', 'body': 'My Body'}
        response = post_request(self.url+'/posts', payload)
        verifictions.verify_equals( response.status_code,201)

    def test_03_delete_post(self):
        response = delete_request(self.url+'/posts', "/101")
        verifictions.verify_equals(response.status_code, 200)
