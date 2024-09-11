import pytest
import requests
from constants import URL

@pytest.fixture()
def get_token(username='raphael', password='cool-but-crude'):
    log_pass = {'username':username, 'password':password}
    resp_token = requests.post(URL + '/auth/login', json=log_pass)
    token = resp_token.json()['userToken']
    return token
