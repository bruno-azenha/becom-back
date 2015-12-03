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

class BeaconSimpleSerializer(serializers.ModelSerializer):
	id_text = serializers.SlugRelatedField(
		read_only=True,
		allow_null=True,
		slug_field='text'
	)
	# id_picture = serializers.SlugRelatedField(
	# 	read_only=True,
	# 	allow_null=True,
	# 	slug_field='picture'
	# )
	picture = serializers.SerializerMethodField('get_picture_url')
	def get_picture_url(self, beacon):
		if beacon.id_picture is not None:
			return beacon.id_picture.picture.url 

	video = serializers.SerializerMethodField('get_video_url')
	def get_video_url(self, beacon):
		if beacon.id_video is not None:
			return beacon.id_video.video.url

	# id_picture = serializers.FileField(
	# 	use_url=True
	# )
	# id_video = serializers.SlugRelatedField(
	# 	read_only=True,
	# 	allow_null=True,
	# 	slug_field='video'
	# )

	class Meta:
		model = Beacon
		fields = ('id', 'user', 'position', 'creation_date', 'expiration_date', 'reach', 'id_text', 'picture', 'video')