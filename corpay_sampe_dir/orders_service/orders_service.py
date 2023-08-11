import os
from abc import ABC
import requests
from rest_framework.exceptions import PermissionDenied
from requests.exceptions import RequestException


class OrdersService(ABC):
    def __init__(self, client_payout_partner=ClientPayoutPartner):
        super().__init__()
        api_keys = client_payout_partner.api_keys if client_payout_partner else None
        if not api_keys or not api_keys.get('api_key', None) or not api_keys.get('secret', None):
            raise PermissionDenied("Your account has not been yet configure to perform OrdersService API operations")

    def post_book_cancel_quote(self):
        uri = f"partner/{partner_id}/{client_code}/orders/{ord_num}/cancel/book"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.post(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def post_cancel_quote(self):
        uri = f"partner/{partner_id}/{client_code}/orders/{ord_num}/cancel/quotes"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.post(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def get_view_orders(self):
        uri = f"partner/{partner_id}/{client_code}/orders/{ord_num}"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.get(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def post_spot_quote(self):
        uri = f"partner/{partner_id}/{client_code}/quotes"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
            'Content-Type': 'application/json',
        }
        response = request.post(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def post_book_quote(self):
        uri = f"partner/{partner_id}/{client_code}/quotes/{quote_id}/book"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.post(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def post_instruct(self, validated_data):
        uri = f"partner/{partner_id}/{client_code}/orders/{ord_num}/instruct"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.post(
            uri, json=validated_data,headers=headers)
        response.raise_for_status()
        return response, validated_data


