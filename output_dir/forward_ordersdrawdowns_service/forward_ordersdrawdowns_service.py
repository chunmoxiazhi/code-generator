import os
from abc import ABC
import requests
from rest_framework.exceptions import PermissionDenied
from zed.exceptions import PayoutServiceError
from mto.models import ClientPayoutPartner


class ForwardOrdersdrawdownsService(ABC):
    def __init__(self, client_payout_partner=ClientPayoutPartner):
        super().__init__()
        api_keys = client_payout_partner.api_keys if client_payout_partner else None
        if not api_keys or not api_keys.get('api_key', None) or not api_keys.get('secret', None):
            raise PermissionDenied("Your account has not been yet configure to perform ForwardOrdersdrawdownsService API operations")

    def get_view_drawdown(self):
        uri = f"partner/{partner_id}/{client_code}/forwards/drawdowns"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.get(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def post_drawdown_instruct(self):
        uri = f"partner/{partner_id}/{client_code}/forwards/drawdowns"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.post(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def get_view_forward(self):
        uri = f"partner/{partner_id}/{client_code}/forwards/{forward_id}"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.get(
            uri, headers=headers)
        response.raise_for_status()
        return response


