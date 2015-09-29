from django.db import models

# Create your models here.
class HelloClass(models.Model):
	HelloString = CharField(max_length=100)

