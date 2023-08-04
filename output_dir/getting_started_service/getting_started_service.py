import os
from abc import ABC
import requests
from rest_framework.exceptions import PermissionDenied
from zed.exceptions import PayoutServiceError
from mto.models import ClientPayoutPartner


class GettingStartedService(ABC):
    def __init__(self, client_payout_partner=ClientPayoutPartner):
        super().__init__()
        api_keys = client_payout_partner.api_keys if client_payout_partner else None
        if not api_keys or not api_keys.get('api_key', None) or not api_keys.get('secret', None):
            raise PermissionDenied("Your account has not been yet configure to perform GettingStartedService API operations")

    def post___spot_quote(self, validated_data):
        uri = f"partner/{partner_id}/{client_code}/quotes"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
            'Content-Type': 'application/json',
        }
        response = request.post(
            uri, json=validated_data,headers=headers)
        response.raise_for_status()
        return response, validated_data

    def post___book_quote_(self):
        uri = f"partner/{partner_id}/{client_code}/quotes/{quote_id}/book"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.post(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def post__instruct_(self):
        uri = f"partner/{partner_id}/{client_code}/orders/{ord_num}/instruct"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.post(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def get__beneficiary_guide_(self, **kwargs):
        template_type = kwargs.get('template_type', None) 
        payment_methods = kwargs.get('payment_methods', None) 
        bank_currency = kwargs.get('bank_currency', None) 
        bankcountry = kwargs.get('bankcountry', None) 
        destinationcountry = kwargs.get('destinationcountry', None) 
        classification = kwargs.get('classification', None) 
        uri = f"templateType={template_type}&paymentMethods={payment_methods}&bankCurrency={bank_currency}&bankcountry={bankcountry}&destinationcountry={destinationcountry}&classification={classification}"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.get(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def post__createedit_bene_(self, validated_data):
        uri = f"partner/{partner_id}/{client_code}/beneficiaries/{bene_id}"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
            'Content-Type': 'application/json',
        }
        response = request.post(
            uri, json=validated_data,headers=headers)
        response.raise_for_status()
        return response, validated_data


