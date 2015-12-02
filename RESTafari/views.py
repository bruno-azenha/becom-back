from django.core.serializers import serialize
from django.contrib.gis.geos import *
from django.contrib.gis.measure import D # ``D`` is a shortcut for ``Distance``

from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from RESTafari.models import *
from RESTafari.serializers import *


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
@permission_classes((AllowAny, ))
def GetNearBeacons(request):
	print("Got into GetNearBeacons")

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


	# Serializes query and returns response
	#response = HttpResponse(BeaconSerializer(query, many=True).data, content_type="application/json")
	return Response(BeaconSimpleSerializer(query, many=True).data)


# API endpoint that given an Beacon ID, returns the beacon and
# all information associated with it
@api_view()
@permission_classes((AllowAny, ))
def GetBeacon(request):
	print("Got into GetBeacon view")
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
def CreateBeacon(request):
	print("Got into CreateBeacon")
	

#API endpoint that gets a Picture stored on the server
@api_view()
@permission_classes((AllowAny, ))
def GetPicture(request):
	picture_id = int(request.GET.get("id"))
	print("Requested Picture Id = " + str(picture_id))

	picture_data = Picture.objects.get(id=picture_id).picture.url
	return Response(picture_data)

#API endpoint that gets a Video stored on the server
@api_view()
@permission_classes((AllowAny, ))
def GetVideo(request):
	video_id = int(request.GET.get("id"))
	print("Requested Video Id = " + str(video_id))

	video_data = Video.objects.get(id=video_id).video.url
	return Response(video_data)







