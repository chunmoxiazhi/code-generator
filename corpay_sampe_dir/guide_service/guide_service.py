import os
from abc import ABC
import requests
from rest_framework.exceptions import PermissionDenied
from requests.exceptions import RequestException


class GuideService(ABC):
    def __init__(self, client_payout_partner=ClientPayoutPartner):
        super().__init__()
        api_keys = client_payout_partner.api_keys if client_payout_partner else None
        if not api_keys or not api_keys.get('api_key', None) or not api_keys.get('secret', None):
            raise PermissionDenied("Your account has not been yet configure to perform GuideService API operations")

    def get_beneficiary_guide(self, **kwargs):
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

    def get_search_banks(self, **kwargs):
        query = kwargs.get('query', None) 
        country = kwargs.get('country', None) 
        uri = f"query={query}&country={country}"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.get(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def get_view_cities(self):
        uri = f"partner/{partner_id}/{client_code}/guides/{country_iso}/{region_name}/cities"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.get(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def get_view_countries(self):
        uri = f"partner/{partner_id}/{client_code}/guides/countries"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.get(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def get_view_currencies(self, **kwargs):
        product = kwargs.get('product', None) 
        uri = f"product={product}"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.get(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def get_forward_guide(self):
        uri = f"partner/{partner_id}/{client_code}/guides/forwardGuide"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.get(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def get_view_regions(self, **kwargs):
        country = kwargs.get('country', None) 
        uri = f"country={country}"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.get(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def post_validation(self):
        uri = f"partner/{partner_id}/{client_code}/guides/validate"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.post(
            uri, headers=headers)
        response.raise_for_status()
        return response


