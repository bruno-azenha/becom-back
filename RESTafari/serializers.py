from rest_framework import serializers
from RESTafari.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'fb_uid', 'email')

class BeaconSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Beacon
		fields = ('id', 'user', 'position', 'creation_date', 'expiration_date', 'reach', 'id_text', 'id_picture', 'id_video')

class TextSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Text
		fields = ('id', 'text',)

class PictureSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Picture
		fields = ('id', 'picture',)

class VideoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Video
		fields = ('id', 'video',)

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		fields = ('id', 'beacon', 'text')
