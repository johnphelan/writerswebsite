from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	bio = models.TextField(default='enter bio text here')
	instagram = models.CharField(default='', max_length=100, blank=True)  
	twitter = models.CharField(default='', max_length=100, blank=True)
	facebook = models.CharField(default='', max_length=100, blank=True)
	linkedin = models.CharField(default='', max_length=100, blank=True)

	def __str__(self):
		return f'{self.user.username} Profile'


class Social(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=200)
	link = models.URLField(max_length=200, blank=True, default='') 
	

	def __str__(self):
		return self.title


	#def save(self):
	#	super().save()
	#
	#	img = Image.open(self.image.path)
	#
	#	if img.height > 300 or img.width > 300:
	#		output_size = (300, 300)
	#		img.thumbnail(output_size)
	#		img.save(self.image.path)
