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
	# Gets latitude and longitude from http request
	lat = request.GET.get('lat')
	lng = request.GET.get('lng')

	# Sets query distance to dist or 100m if dist is not set
	dist = request.GET.get('dist') if request.GET.get('dist') == '' else 100

	# Creates a point from to calculate distances from
	point = fromstr('POINT({0} {1})'.format(lat, lng), srid=4326)

	# Gets all beacons within dist from point
	query = Beacon.objects.filter(position__distance_lte=(point, dist, 'spheroid'))
	
	# Serializes query and returns response
	response = HttpResponse(serialize('geojson', query), content_type="application/json")
	return (response)
