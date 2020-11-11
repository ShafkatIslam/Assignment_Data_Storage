from rest_framework import serializers

from stores_data.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','street','city','state','zip']

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','belong_to']
