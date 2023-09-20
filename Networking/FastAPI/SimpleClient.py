import requests
from http import HTTPStatus

from Collections import Dict

endpoint: str = "http://0.0.0.0:52525"


# Will call http://localhost:52525/ --> the hello() method of the server will be invoked
def simple_GET_request():
    response = requests.get(endpoint + "/")
    if HTTPStatus.OK == response.status_code:  # HTTP_OK
        print(response.text)
        # print(response.json())
    else:
        print(f"Error {response.status_code}")


# Will call http://localhost:52525/greeting --> the hello() method of the server will be invoked
#                                               with HTTP GET params: name = 'Some_Test_Name'
def simple_GET_request_with_params():
    get_query_params: Dict = {'name': 'Some_Test_Name'}
    response = requests.get(endpoint + "/greeting", params=get_query_params)
    if HTTPStatus.OK == response.status_code:  # HTTP_OK
        # print(response.text)
        print(response.json())
    else:
        print(f"Error {response.status_code}")


def simple_POST_request():
    query_params = {"key": "One", "value": "I"}
    response = requests.post(endpoint + "/store_some_data", params=query_params)
    if HTTPStatus.OK == response.status_code:  # HTTP_OK
        # print(response.text)
        print(response.json())
    else:
        print(f"Error {response.status_code}")


if __name__ == '__main__':
    # simple_GET_request()
    # simple_GET_request_with_params()
    simple_POST_request()
