from django.contrib.gis.db import models

# Create your models here.
class Text(models.Model):
	text = models.TextField()

class Picture(models.Model):
	picture = models.FileField(upload_to="user_pic")

class Video(models.Model):
	video = models.FileField(upload_to="user_vid")


class User(models.Model):
	email  = models.EmailField()
	name   = models.CharField(100)
	age    = models.IntField(null=true)
	gender = models.IntField(null=true)        

class Beacon(models.Model):
	user            = models.ForeignKey(User)
	position        = models.PointField()
	creation_date   = models.DateTimeField(auto_now_add=True)
	expiration_date = models.DateTimeField()
	reach           = models.FloatField(default=20.0)
	id_text         = models.ForeignKey(Text, null=True)
	id_picture      = models.ForeignKey(Picture, null=True)
	id_video        = models.ForeignKey(Video, null=True)

class Comment(models.Model):
	beacon = models.ForeignKey(Beacon)
	text   = models.ForeignKey(Text)

    