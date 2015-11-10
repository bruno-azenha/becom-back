from django.http import JsonResponse
from RESTafari.models import *
from RESTafari.models import Beacon
from RESTafari.serializers import UserSerializer, BeaconSerializer

from django.contrib.gis.geos import *
from django.contrib.gis.measure import D # ``D`` is a shortcut for ``Distance``

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
	lat = request.GET.get('lat')
	lng = request.GET.get('lng')

	point = fromstr('POINT({0} {1})'.format(lat, lng), srid=4326)

	#query = Beacon.objects.filter(position__distance_lte=(point, D(m=20)))

	response = JsonResponse([1,2], safe=False)
	print(response)
	return (response)
