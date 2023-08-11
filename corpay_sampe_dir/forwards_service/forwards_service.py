import os
from abc import ABC
import requests
from rest_framework.exceptions import PermissionDenied
from requests.exceptions import RequestException


class ForwardsService(ABC):
    def __init__(self, client_payout_partner=ClientPayoutPartner):
        super().__init__()
        api_keys = client_payout_partner.api_keys if client_payout_partner else None
        if not api_keys or not api_keys.get('api_key', None) or not api_keys.get('secret', None):
            raise PermissionDenied("Your account has not been yet configure to perform ForwardsService API operations")

    def get_view_forward_quote(self):
        uri = f"partner/{partner_id}/{client_code}/forwardQuote/{quote_id}"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.get(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def post_forward_quote(self):
        uri = f"partner/{partner_id}/{client_code}/forwardQuotes"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
            'Content-Type': 'application/json',
        }
        response = request.post(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def post_book_forward_quote(self):
        uri = f"partner/{partner_id}/{client_code}/forwardQuotes/{quote_id}/book"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.post(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def post_complete_order(self):
        uri = f"partner/{partner_id}/{client_code}/forwards/{forward_id}/completeOrder"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.post(
            uri, headers=headers)
        response.raise_for_status()
        return response


