import os
from abc import ABC
import requests
from rest_framework.exceptions import PermissionDenied
from requests.exceptions import RequestException


class BatchPaymentsService(ABC):
    def __init__(self, client_payout_partner=ClientPayoutPartner):
        super().__init__()
        api_keys = client_payout_partner.api_keys if client_payout_partner else None
        if not api_keys or not api_keys.get('api_key', None) or not api_keys.get('secret', None):
            raise PermissionDenied("Your account has not been yet configure to perform BatchPaymentsService API operations")

    def post_batch_payments_quote(self, validated_data):
        uri = f"partner/{partner_id}/{client_code}/payment-quotes"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.post(
            uri, json=validated_data,headers=headers)
        response.raise_for_status()
        return response, validated_data

    def post_book_batch_payments(self, **kwargs):
        quote_id = kwargs.get('quote_id', None) 
        login_session_id = kwargs.get('login_session_id', None) 
        uri = f"quoteId={quote_id}&loginSessionId={login_session_id}"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.post(
            uri, headers=headers)
        response.raise_for_status()
        return response


