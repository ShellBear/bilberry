from django.db import models

#Image database
class imageDatas(models.Model):
	image_id = models.IntegerField()
	path = models.CharField(max_length=100)
	timestamp = models.DateTimeField()
	verified = models.BooleanField()
	rejected = models.BooleanField()
