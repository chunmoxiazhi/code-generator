import os
from abc import ABC
import requests
from rest_framework.exceptions import PermissionDenied
from zed.exceptions import PayoutServiceError
from mto.models import ClientPayoutPartner
from zed.utils import check_date_format
from datetime import datetime


class SettlementAccountsService(ABC):
    def __init__(self, client_payout_partner=ClientPayoutPartner):
        super().__init__()
        api_keys = client_payout_partner.api_keys if client_payout_partner else None
        if not api_keys or not api_keys.get('api_key', None) or not api_keys.get('secret', None):
            raise PermissionDenied("Your account has not been yet configure to perform SettlementAccountsService API operations")

    def get_view_settlements(self):
        uri = f"partner/{partner_id}/{client_code}/settlement-accounts"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.get(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def get_view_fxbalance(self, **kwargs):
        search_string = kwargs.get('search_string', None) 
        include_balance = kwargs.get('include_balance', None) 
        uri = f"searchString={search_string}&includeBalance={include_balance}"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.get(
            uri, headers=headers)
        response.raise_for_status()
        return response

    def get_fxbalance_history(self, link_balance_id, **kwargs):
        from_date = kwargs.get('from_date', None) 
        to_date = kwargs.get('to_date', None) 
        uri = f"fromDate={from_date}&toDate={to_date}"
        uri = self.HOST + uri
        headers = {
            'CMG-AccessToken': 'Bear token', #pull token from Zed
        }
        response = request.get(
            uri, headers=headers)
        response.raise_for_status()
        return response


