from django.core.serializers import serialize
from django.contrib.gis.geos import *
from django.contrib.gis.measure import D # ``D`` is a shortcut for ``Distance``
from django.db.models import F # For referencing fields in the same model
from django.http import HttpResponse

from RESTafari.models import *

from RESTafari.serializers import *

from rest_framework import viewsets

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
def GetNearBeacons(request):
	# Gets latitude, longitude and distance from http request
	lat = request.GET.get('lat')
	lng = request.GET.get('lng')

	# Creates a point from to calculate distances from
	point = fromstr('POINT({0} {1})'.format(lat, lng), srid=4326)

	# Gets all beacons within range of the point
	query = Beacon.objects.all().extra(where=['ST_Distance(position, ST_PointFromText(%s, 4326)) <= CAST(reach AS double precision) / 1000'], params=[point.wkt] ) 

	print (query)
	# Serializes query and returns response
	response = HttpResponse(serialize('geojson', query), content_type="application/json")
	return (response)
