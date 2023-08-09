import os
from abc import ABC
import requests
from rest_framework.exceptions import PermissionDenied
from zed.exceptions import PayoutServiceError


class PaymentWithoutLiabilityShiftService(ABC):
    def __init__(self):
        super().__init__()

    def post_payment_without_liability_shift(self, validated_data, url):
        uri = f"{{url}}/ppp/api/payment.do"
        uri = self.HOST + uri
        headers = {
            'Content-Type': 'application/json',
        }
        response = request.post(
            uri, json=validated_data,headers=headers)
        response.raise_for_status()
        return response, validated_data


