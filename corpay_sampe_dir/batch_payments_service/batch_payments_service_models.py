from rest_framework import serializers

class BatchPaymentsQuoteSerializer(serializers.Serializer):
    payments = PaymentsSerializer()
    settlements = SettlementsSerializer()

class PaymentsSerializer(serializers.Serializer):
    beneficiary_id = serializers.CharField()
    amount = serializers.FloatField()
    currency = serializers.CharField()
    payment_method = serializers.CharField()
    purpose_of_payment = serializers.CharField()
    remitter_id = serializers.CharField()
    payment_reference = serializers.CharField()
    delivery_date = serializers.CharField()
    lock_side = serializers.CharField()

class SettlementsSerializer(serializers.Serializer):
    account_id = serializers.CharField()
    method = serializers.CharField()
    currency = serializers.CharField()


request_body_sample = [ {
  "payments" : 
            {
            "beneficiaryId": "Resource10-2",
            "amount": 1000,
            "currency": "EUR",
            "paymentMethod": "Wire",
            "purposeOfPayment":"",
            "remitterId": "",
            "paymentReference": "",
            "DeliveryDate": "2021-01-30",
            "lockSide": "Payment"
            },
  "settlements" : 
            {
            "accountId":"INCOMING-TEST-USD" ,
            "Method":"Wire",
            "currency":"USD"    
            }
  }, 
     {
  "payments" : 
            {
            "beneficiaryId": "inr123",
            "amount": 1000,
            "currency": "INR",
            "paymentMethod": "Wire",
            "purposeOfPayment":"",
            "remitterId": "",
            "paymentReference": "",
            "DeliveryDate": "2021-01-30",
            "lockSide": "Payment"
            },
  "settlements" : 
            {
            "accountId":"INCOMING-TEST-USD" ,
            "Method":"Wire",
            "currency":"USD"    
            }
  }   ]
class BookBatchPaymentsQueryParameterSerializer(serializers.Serializer):
    quote_id = serializers.CharField()
    login_session_id = serializers.CharField()


