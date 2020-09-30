from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class Minigame73(models.Model):
	username = models.CharField(max_length=50)
	#data = models.CharField(max_length=1000)
	data = models.BinaryField()
	#author = models.ForeignKey(User, on_delete = models.DO_NOTHING)

