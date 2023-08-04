import os
from abc import ABC
import requests
from rest_framework.exceptions import PermissionDenied
from zed.exceptions import PayoutServiceError
from mto.models import ClientPayoutPartner


class AuthenticationService(ABC):
    def __init__(self, client_payout_partner=ClientPayoutPartner):
        super().__init__()
        api_keys = client_payout_partner.api_keys if client_payout_partner else None
        if not api_keys or not api_keys.get('api_key', None) or not api_keys.get('secret', None):
            raise PermissionDenied("Your account has not been yet configure to perform AuthenticationService API operations")

    def post_token_authentication(self, validated_data):
        uri = f"partner/{partner_id}/tokens"
        uri = self.HOST + uri
        headers = {
            'AccessToken': 'Bear token', #pull token from Zed
            'Content-Type': 'application/json',
        }
        response = request.post(
            uri, json=validated_data,headers=headers)
        response.raise_for_status()
        return response, validated_data


