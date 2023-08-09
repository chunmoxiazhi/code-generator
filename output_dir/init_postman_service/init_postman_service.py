import os
from abc import ABC
import requests
from rest_framework.exceptions import PermissionDenied
from zed.exceptions import PayoutServiceError


class InitPostmanService(ABC):
    def __init__(self):
        super().__init__()

    def get_init_postman(self):
        uri = f"http://safecharge.com"
        uri = self.HOST + uri
        headers = {
        }
        response = request.get(
            uri, headers=headers)
        response.raise_for_status()
        return response


