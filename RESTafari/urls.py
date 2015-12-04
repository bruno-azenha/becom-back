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

	url(r'^beacons/$', views.near_beacons),
	url(r'^beacon/$', views.beacon),
	url(r'^beacon/create$', views.create_beacon),

	url(r'^pictures/(\d+)$', views.picture),
	url(r'^videos/(\d+)$', views.video),
	url(r'^texts/(\d+)$', views.text),

	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]