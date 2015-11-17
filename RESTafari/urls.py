from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'beacons', views.BeaconViewSet)
router.register(r'texts', views.TextViewSet)
router.register(r'pictures', views.PictureViewSet)
router.register(r'videos', views.VideoViewSet)
router.register(r'comments', views.CommentViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	url(r'^browsable_api/', include(router.urls)),

	url(r'^beacons/$', views.GetNearBeacons),
	url(r'^beacon/$', views.GetBeacon),

	url(r'^picture/$', views.GetPicture),

	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]