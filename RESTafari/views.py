from RESTafari.models import *
#from RESTafari.quickstart.serializers import UserSerializer, GroupSerializer

from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class BeaconViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows beacons to be viewed or edited.
    """
    queryset = Beacon.objects.all()
    serializer_class = BeaconSerializer