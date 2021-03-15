from rest_framework import serializers 
 
 
class Api1Serializer(serializers.Serializer):
 
    invalid_trigger = serializers.CharField()
    key = serializers.CharField()
    name = serializers.CharField()
    reuse = serializers.BooleanField()
    support_multiple = serializers.BooleanField()
    pick_first = serializers.BooleanField()
    supported_values = serializers.ListField(
        child=serializers.CharField()
    )
    type = serializers.ListField(
        child=serializers.CharField()
    )
    validation_parser = serializers.CharField()
    values = serializers.ListField(
        child=serializers.DictField(child=serializers.CharField())
    )

class Api2Serializer(serializers.Serializer):
 
    invalid_trigger = serializers.CharField()
    key = serializers.CharField()
    name = serializers.CharField()
    reuse = serializers.BooleanField()
    pick_first = serializers.BooleanField()
    type = serializers.ListField(
        child=serializers.CharField()
    )
    validation_parser = serializers.CharField()
    constraint = serializers.CharField()
    var_name = serializers.CharField()
    values = serializers.ListField(
        child=serializers.DictField(child=serializers.CharField())
    )

