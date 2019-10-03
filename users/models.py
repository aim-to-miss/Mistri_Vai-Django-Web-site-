from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	address = models.CharField(max_length = 30, null = True)
	mobile = models.CharField(max_length = 30, null = True)
	image = models.ImageField(default = '123.jpg',upload_to = 'profile_pics')
	def __str__ (self):
		return f'{self.user.username} Profile'




def user_post_save(sender,**kwargs):
	if kwargs['created']:
		profile = Profile.objects.create(user = kwargs['instance'])

post_save.connect(user_post_save,sender = User)
