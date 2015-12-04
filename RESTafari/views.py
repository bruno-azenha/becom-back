# -*- coding: utf-8 -*-

from django.core.serializers import serialize
from django.contrib.gis.geos import *
from django.contrib.gis.measure import D # ``D`` is a shortcut for ``Distance``
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from RESTafari.models import *
from RESTafari.serializers import *

from base64 import b64decode
from django.core.files.base import ContentFile

import json
import datetime
import pytz
import uuid

# API endpoint that allows users to be viewed or edited.
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

# API endpoint that allows beacons to be viewed or edited.
class BeaconViewSet(viewsets.ModelViewSet): 
	queryset = Beacon.objects.all()
	serializer_class = BeaconSerializer

# API endpoint that allows texts to be viewed or edited.
class TextViewSet(viewsets.ModelViewSet):
	queryset = Text.objects.all()
	serializer_class = TextSerializer

# API endpoint that allows pictures to be viewed or edited.
class PictureViewSet(viewsets.ModelViewSet):
	queryset = Picture.objects.all()
	serializer_class = PictureSerializer

# API endpoint that allows videos to be viewed or edited.
class VideoViewSet(viewsets.ModelViewSet):
	queryset = Video.objects.all()
	serializer_class = VideoSerializer

# API endpoint that allows comments to be viewed or edited.
class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

# API endpoint that returns all beacons that are on reach of a certain
# coordinate (lat, lng)
@api_view()
@permission_classes((IsAuthenticated, ))
def near_beacons(request):
	# Gets latitude, longitude and distance from http request
	lat = request.GET.get('lat')
	lng = request.GET.get('lng')
	dist = request.GET.get('dist')

	# Creates a point from to calculate distances from
	point = fromstr('POINT({0} {1})'.format(lat, lng), srid=4326)

	# Verifies if dist parameter was passed
	if dist == None:
		# Gets all beacons within range of the point
		query = Beacon.objects.all().extra(where=['(ST_Distance(position, ST_PointFromText(%s, 4326))) <= CAST(reach AS double precision)'], params=[point.wkt]) 

	else:
		# Gets all beacon within dist distance from point
		dist = int(dist)
		query = Beacon.objects.filter(position__distance_lte=(point, D(m=dist)))

	now = datetime.datetime.now().replace(tzinfo=pytz.UTC)
	query = [x for x in query if x.expiration_date>now]

	# Serializes query and returns response
	#response = HttpResponse(BeaconSerializer(query, many=True).data, content_type="application/json")
	return Response(BeaconSimpleSerializer(query, many=True).data)

# API endpoint that given an Beacon ID, returns the beacon and
# all information associated with it
@api_view()
@permission_classes((IsAuthenticated, ))
def my_beacons(request):
	query = Beacon.objects.filter(user=request.user)
	return Response(BeaconSimpleSerializer(query, many=True).data)



# API endpoint that given an Beacon ID, returns the beacon and
# all information associated with it
@api_view()
@permission_classes((IsAuthenticated, ))
def beacon(request):

	if request.method == 'GET':

		# Get id from http request
		beacon_id = int(request.GET.get('id'))

		# Select correct beacon
		beacon = Beacon.objects.get(id=beacon_id)

		# Retrieves ids for text, picture and video if exist
		text = beacon.id_text.text if beacon.id_text != None else None
		picture = beacon.id_picture.id if beacon.id_picture != None else None
		video = beacon.id_video.id if beacon.id_video != None else None

		#print("textID:{0}  pictureID:{1}  videoID:{2}".format(textId.text, pictureId, videoId))

		# Encapsulate text, picture url and video url
		data = dict([('text', text), ('picture', picture), ('video', video)])
		
		# Serialize data into requested content-type and return
		return Response(data)


#API endpoint that given all of its information, creates a beacon
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def create_beacon(request):
	if request.method == 'POST':
		received_json = json.loads(request.body.decode('utf-8'))

		lat = received_json['lat']
		lng = received_json['lng']

		if (not request.user.is_authenticated()):
			HttpResponse("fudeu")

		beacon = Beacon()
		beacon.user = request.user
		beacon.position = fromstr('POINT({0} {1})'.format(lat, lng), srid=4326)
		beacon.expiration_date = datetime.datetime.now().replace(tzinfo=pytz.UTC) + datetime.timedelta(1)

		if 'text' in received_json:
			text = Text(text=received_json['text'])
			text.save()
			beacon.id_text = text

		if 'picture' in received_json:
			picture_data = b64decode(received_json['picture'])
			picture = Picture(picture=ContentFile(picture_data, name=str(uuid.uuid1())+'.jpg'))
			picture.save()
			beacon.id_picture = picture

		if 'video' in request.FILES:
			video = Video(video=request.FILES['video'])
			video.save()
			beacon.id_video = video

		beacon.save()

		return HttpResponse(status=status.HTTP_200_OK)

	else:
		return HttpResponse(status=status.HTTP_200_OK)


#API endpoint that gets a Picture stored on the server
@api_view()
@permission_classes((IsAuthenticated, ))
def picture(request, id):
	print("Requested Picture Id = " + id)

	picture_data = Picture.objects.get(id=id).picture.url
	return Response(picture_data)

#API endpoint that gets a Video stored on the server
@api_view()
@permission_classes((IsAuthenticated, ))
def video(request, id):
	print("Requested Video Id = " + id)

	video_data = Video.objects.get(id=id).video.url
	return Response(video_data)

#API endpoint that gets a Text stored on the server
@api_view()
@permission_classes((IsAuthenticated, ))
def text(request, id):
	print("Requested text Id = " + id)

	text_data = Text.objects.get(id=id).text
	return Response(text_data)

