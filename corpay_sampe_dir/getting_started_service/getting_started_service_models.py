from rest_framework import serializers

class BeneficiaryGuideQueryParameterSerializer(serializers.Serializer):
    template_type = serializers.CharField()
    payment_methods = serializers.CharField()
    bank_currency = serializers.CharField()
    bankcountry = serializers.CharField()
    destinationcountry = serializers.CharField()
    classification = serializers.CharField()

class CreateEditBeneSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    template_data = TemplatedataSerializer()
    payment_data = PaymentdataSerializer()

class TemplatedataSerializer(serializers.Serializer):
    bene_data = BenedataSerializer()
    bank_data = BankdataSerializer()

class BenedataSerializer(serializers.Serializer):
    bene_specific = BenespecificSerializer()
    address = AddressSerializer()

class BenespecificSerializer(serializers.Serializer):
    account_holder_name = serializers.CharField()
    classification = serializers.CharField()
    account_number = serializers.CharField()
    local_account_number = serializers.CharField()
    phone_number = serializers.CharField()
    email_address = serializers.CharField()

class AddressSerializer(serializers.Serializer):
    country = serializers.CharField()
    region = serializers.CharField()
    city = serializers.CharField()
    address_line1 = serializers.CharField()
    address_line2 = serializers.CharField()
    postal_code = serializers.CharField()

class BankdataSerializer(serializers.Serializer):
    bank_specific = BankspecificSerializer()
    address = AddressSerializer()
    regulatory_data = RegulatorydataSerializer()

class BankspecificSerializer(serializers.Serializer):
    name = serializers.CharField()
    routing_code = serializers.CharField()
    local_routing_code = serializers.CharField()
    swiftbic = serializers.CharField()

class AddressSerializer(serializers.Serializer):
    country = serializers.CharField()
    region = serializers.CharField()
    city = serializers.CharField()
    address_line1 = serializers.CharField()
    address_line2 = serializers.CharField()
    postal_code = serializers.CharField()

class RegulatorydataSerializer(serializers.Serializer):
    regulatory = RegulatorySerializer()

class RegulatorySerializer(serializers.Serializer):

class PaymentdataSerializer(serializers.Serializer):
    payment_specific = PaymentspecificSerializer()

class PaymentspecificSerializer(serializers.Serializer):
    payment_currency = serializers.CharField()
    send_paytracker = serializers.FloatField()
    preferred_method = serializers.CharField()
    payment_alert = serializers.CharField()


request_body_sample = {

 	"identifier": "testdemobeneINR2",
 	"templateData": {
 		"beneData": {
 			"beneSpecific": {
 				"accountHolderName": "john",
 				"classification": "Individual",
 				"accountNumber": "67385863631",
 				"localAccountNumber": "",
 				"phoneNumber": "",
 				"emailAddress": ""
 			},
 			"address": {
 				"country": "CA",
 				"region": "ON",
 				"city": "Toronto",
 				"addressLine1": "234 king st",
 				"addressLine2": "",
 				"postalCode": "m5a2r4"
 			}
 		},
 		"bankData": {
 			"bankSpecific": {
 				"name": "State Bank of India",
 				"routingCode": "34356456987",
 				"localRoutingCode": "SBIN0070706",
 				"SWIFTBIC": "SBININBBXXX"

 			},
 			"address": {
 				"country": "IN",
 				"region": "Kerla",
 				"city": "Kochi",
 				"addressLine1": "No.37/2156 A5, Madathikunnel Buildi",
 				"addressLine2": "",
 				"postalCode": "682017"

 			},

 			"regulatoryData": {
 				"regulatory": {
 					"regulatorySpecific": [{
 						"key": "BeneficiaryAccountType",
 						"value": "CACC"


 					}]

 				}
 			}

 		}

 	},

 	"paymentData": {
 		"paymentSpecific": {
 			"paymentMethod": ["E"],
 			"paymentCurrency": "INR",
 			"sendPaytracker": false,
 			"preferredMethod": "E",
 			"paymentAlert": ""
 		}

 	}



 }

