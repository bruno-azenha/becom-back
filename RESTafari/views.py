from django.core.serializers import serialize
from django.contrib.gis.geos import *
from django.contrib.gis.measure import D # ``D`` is a shortcut for ``Distance``
from django.http import HttpResponse

from RESTafari.models import *

from RESTafari.serializers import UserSerializer, BeaconSerializer

from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BeaconViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows beacons to be viewed or edited.
    """
    queryset = Beacon.objects.all()
    serializer_class = BeaconSerializer


def GetNearBeacons(request):
	# Gets latitude, longitude and distance from http request
	lat = request.GET.get('lat')
	lng = request.GET.get('lng')
	dist = request.GET.get('dist')

	# Sets query distance to dist or 100m if dist is not set
	dist = 100 if dist == '' else int(dist)
	print ("Dist is: {}".format(dist))
	# Creates a point from to calculate distances from
	point = fromstr('POINT({0} {1})'.format(lat, lng), srid=4326)

	# Gets all beacons within dist from point
	print (D(m=dist))
	query = Beacon.objects.filter(position__distance_lte=(point, D(m=dist)))
	print (query)
	# Serializes query and returns response
	response = HttpResponse(serialize('geojson', query), content_type="application/json")
	return (response)
