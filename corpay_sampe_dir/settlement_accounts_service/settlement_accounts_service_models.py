from rest_framework import serializers

class ViewFxbalanceQueryParameterSerializer(serializers.Serializer):
    search_string = serializers.CharField()
    include_balance = serializers.BooleanField()

class FxbalanceHistoryQueryParameterSerializer(serializers.Serializer):
    from_date = serializers.CharField() #{YYYY-MM-DD}
    to_date = serializers.CharField() #{YYYY-MM-DD}


