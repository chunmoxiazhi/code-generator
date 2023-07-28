
config_mapper_sample = '''
# This is an example of recursive mapping method
def config_mapper(snake_str):
    if isinstance(snake_str, dict):
        camel_dict = {}
        for key, value in snake_str.items():
            camel_key = config_mapper(key)
            camel_dict[camel_key] = config_mapper(value)
        return camel_dict

    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def generate_request_body(request_body): 
    camel_dict = {}
    for key, value in request_body.items():
        camel_key = config_mapper(key)
        if isinstance(value, dict):
            camel_dict[camel_key] = config_mapper(value)
        else:
            camel_dict[camel_key] = value
    return camel_dict
'''

SRC_BENE_LOOKUP = {
    #beneData
    'identifier': 'recipient.remote_id',
    'accountHolderName': 'recipient.first_name' + 'recipient.last_name',
    'classification': 'recipient.account_type',
    'accountNumber': 'wallet.account_number',
    'bank_account_number': 'wallet.account_number',
    'account_number': 'wallet.account_number', 
    # "localAccountNumber": 'recipient.first_name',
    'phoneNumber': 'wallet.mobile_number',
    "emailAddress": 'recipient.email',
    "country": 'recipient.address.country',
    "region": 'recipient.address.province',
    "city": 'recipient.address.city',
    "addressLine1": 'recipient.address.address_line_one',
    "addressLine2": 'recipient.address.address_line_two',
    "postalCode": 'recipient.address.postal_code',

    #bankData
    "name": 'wallet.bank_name',
    'routingCode': 'wallet.bank_routing',
    #'localRoutingCode': 'wallet.bank_routing',
    'SWIFTBIC': 'wallet.bank_swift_bic',
    "country": 'wallet.bank_country_code',
    #"region": 'wallet.province',
    #"city": 'wallet.city',
    "addressLine1": "wallet.bank_address",
    #"addressLine2": "wallet.bank_address",
    "postalCode": "wallet.postal_code"

    #regulatorySpecific
}

SRC_SPOT_QUOTE_LOOKUP = {
    'paymentCurrency': 'sell_currency',
    'settlementCurrency': 'buy_currency',
    'amount': 'amount',
    'lockSide': 'is_amount_settlement'
}
