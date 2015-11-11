from rest_framework import serializers
from RESTafari.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'name', 'age', 'gender', 'fb_uid', 'fb_token')

class BeaconSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Beacon
		fields = ('id', 'user', 'position', 'creation_date', 'expiration_date', 'reach', 'id_text', 'id_picture', 'id_video')

class TextSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Text
		fields = ('text',)

class PictureSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Picture
		fields = ('picture',)

class VideoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Video
		fields = ('video',)

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		fields = ('beacon', 'text')
