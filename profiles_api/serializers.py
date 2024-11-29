from rest_framework import serializers


class hello_serializers(serializers.Serializer):
    name = serializers.CharField(max_length=10)




