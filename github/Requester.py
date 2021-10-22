import requests
import json


class Requester:
    def __init__(self, id_or_token: str, password:str, base_url: str):
        self._id_or_token = id_or_token
        self._password = password
        self._base_url = base_url

    def _check_status(self, res: json, success_code: int = 200):
        if res.status_code is success_code:
            return True
        else:
            return False

    def _separate_request_type(self, headers: str, request_type: str, full_url: str, update_data: str):
        request_type: str = request_type.upper()

        if request_type == 'GET':
            return requests.get(full_url, headers=headers)

        elif request_type == 'POST':
            return requests.post(full_url, headers=headers)

        elif request_type == 'PATCH':
            if update_data is None:
                return

            return requests.patch(full_url, headers=headers)

        elif request_type == 'DELETE':
            return requests.delete(full_url, headers=headers)

        else:
            return

    def request_to_hub(self, headers: str, request_type: str, route: str, update_data: str=None, success_code: int = 200):
        full_url: str = self._base_url + route

        res = self._separate_request_type(
            headers, request_type, full_url, update_data)
        succeed_in_receiving_response = self._check_status(res, success_code)

        if succeed_in_receiving_response:
            return res.json()
        else:
            return
