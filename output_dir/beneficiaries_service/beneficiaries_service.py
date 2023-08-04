import os
from abc import ABC
import requests
from rest_framework.exceptions import PermissionDenied
from zed.exceptions import PayoutServiceError
from mto.models import ClientPayoutPartner


class BeneficiariesService(ABC):
    def __init__(self, client_payout_partner=ClientPayoutPartner):
        super().__init__()
        api_keys = client_payout_partner.api_keys if client_payout_partner else None
        if not api_keys or not api_keys.get('api_key', None) or not api_keys.get('secret', None):
            raise PermissionDenied("Your account has not been yet configure to perform BeneficiariesService API operations")

    def post_createedit_bene(self, validated_data):
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

    def get_view_bene(self):
        uri = f"partner/{partner_id}/{client_code}/beneficiaries/{bene_id}"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.get(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def delete_delete_bene(self):
        uri = f"partner/{partner_id}/{client_code}/beneficiaries/{bene_id}"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.delete(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def get_list_all_benes(self):
        uri = f"partner/{partner_id}/{client_code}/beneficiaries"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
            'client_id': '252497',
            'client_secret': '111111',
        }
        response = request.get(
            uri, headers=headers)
        response.raise_for_status()
        return response


