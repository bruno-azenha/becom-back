from rest_framework import serializers
from RESTafari.models import User, Beacon

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'name', 'age', 'gender')

class BeaconSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Beacon
		fields = ('user', 'position', 'creation_date', 'expiration_date', 'reach')