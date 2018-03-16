from .models import imageDatas
from django.utils import timezone
from datetime import datetime, timedelta

def get_image_elems():
	elems = len(imageDatas.objects.values_list('image_id', flat=True))
	return elems

def add_image(path):
	image_id = get_image_elems()
	new_image = imageDatas.objects.create(image_id = image_id, path = path,
	timestamp = datetime.now(tz=timezone.utc) + timedelta(hours=1),
	verified = False, rejected = False)
	new_image.save()

def set_image_verified(image_id):
	image = imageDatas.objects.all()[image_id]
	image.verified = True
	image.save()

def set_image_rejected(image_id, rejected):
	if rejected == "true":
		boolean = True
	else:
		boolean = False
	image = imageDatas.objects.all()[image_id]
	image.rejected = boolean
	image.save()
