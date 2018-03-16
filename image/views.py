from django.http import HttpResponse
from django.shortcuts import render
from .database import *
from django.http import Http404
from django.core.files.storage import FileSystemStorage
import os

#The picture extensions
ext = [".png", ".jpeg"]

#Homepage
def index(request):
	return render(request, 'image/index.html')

#Image viewer page
def image_list(request):
	imageList = imageDatas.objects.all()
	for elements in imageList:
		print (elements.path)
	return render(request, 'image/view_all.html', {'imageDatas': imageList})

def image_viewer(request):
	return render(request, 'image/image_viewer.html')

# Simple Uploader
def upload_file(request):
	image = request.FILES['image']
	if image.name.endswith(tuple(ext)):
		imageName = 'uploads/' + image.name
		if (os.path.exists('uploads') != True):
			os.mkdir('uploads')
		fs = FileSystemStorage()
		imageName = fs.save(imageName, image)
		uploaded_file_url = fs.url(imageName)
		add_image(uploaded_file_url)
		return render(request, 'image/upload.html', {
			'upload_message': 'File uploaded at:',
			'uploaded_file_url': uploaded_file_url
		})
	else:
		return render(request, 'image/upload.html', {
			'upload_message': 'Invalid file format',
			'uploaded_file_url': '/upload'
		})

#Image uploader page
def upload(request):
	if request.method == 'POST' and request.FILES:
		return upload_file(request)
	else:
		return render(request, 'image/upload.html', None)

def displayFile(request, file):
	try:
		with open('uploads/' + file, "rb") as f:
			return HttpResponse(f.read(), content_type="image")
	except IOError:
		raise Http404("File doesn't exists!")

#Image viewer
def imageViewer(request, id, rejected, verified):
	elems = get_image_elems()
	if elems == 0:
			raise Http404("File doesn't exists!")
	id = int(id) % elems
	image = imageDatas.objects.all()[id]
	if verified == "true":
		if id == 0:
			id = elems
		id -= 1
		set_image_verified(id)
		set_image_rejected(id, rejected)
	try:
		with open(image.path, "rb") as f:
			return HttpResponse(f.read(), content_type="image")
	except IOError:
		raise Http404("File doesn't exists!")
