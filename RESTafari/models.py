from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
class Text(models.Model):
	text = models.TextField()

class Picture(models.Model):
	picture = models.FileField(upload_to="user_pic")

class Video(models.Model):
	video = models.FileField(upload_to="user_vid")


class Beacom(models.Model):
	user            = models.ForeignKey(User)
	position        = models.PointField()
	creation_date   = models.DateTimeField(auto_now_add=True)
	expiration_date = models.DateTimeField()
	reach           = models.FloatField(default=20.0)
	id_text         = models.ForeignKey(Text, null=True)
	id_picture      = models.ForeignKey(Picture, null=True)
	id_video        = models.ForeignKey(Video, null=True)

    