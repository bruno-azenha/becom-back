from RESTafari.models import *
#from RESTafari.quickstart.serializers import UserSerializer, GroupSerializer

from rest_framework import viewsets
from RESTafari.serializers import UserSerializer, BeaconSerializer


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