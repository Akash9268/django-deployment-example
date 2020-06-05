from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userprofileinfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE) #extending our user 

	#additional
	portfolio_site = models.URLField(blank=True)

	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)


	def __Str__(self):

		return self.user.username