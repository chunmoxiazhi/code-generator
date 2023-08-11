from rest_framework import serializers

class BeneficiaryGuideQueryParameterSerializer(serializers.Serializer):
    template_type = serializers.CharField()
    payment_methods = serializers.CharField()
    bank_currency = serializers.CharField()
    bankcountry = serializers.CharField()
    destinationcountry = serializers.CharField()
    classification = serializers.CharField()

class SearchBanksQueryParameterSerializer(serializers.Serializer):
    query = serializers.CharField()
    country = serializers.CharField() #{country ISO2}

class ViewCurrenciesQueryParameterSerializer(serializers.Serializer):
    product = serializers.CharField()

class ViewRegionsQueryParameterSerializer(serializers.Serializer):
    country = serializers.CharField()


