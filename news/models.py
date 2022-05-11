from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
	code		= models.IntegerField(blank=True, null=True)
	title 		= models.CharField(max_length=100)
	by 			= models.CharField(max_length=100)
	body		= models.TextField(blank=True, null=True)
	urls 		= models.URLField(blank=True, null=True)
	date_time	= models.DateTimeField(default=timezone.now)
	likes		= models.ManyToManyField(User, related_name='blog_posts')
	attached_image 	= models.ImageField(null=True, blank=True, upload_to='images/')

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.title + ' | by:' +str(self.by)+ ' | ' +str(self.date_time)

	def get_absolute_url(self):
		return reverse('article_detail', args=(str(self.id)))

class Comment(models.Model):
	post 		=	models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	by 			= models.CharField(max_length=100)
	body		=	models.TextField(blank=True, null=True)
	date_added 	=	models.DateTimeField(default=timezone.now)

	class Meta:
		ordering	=	['-date_added']

	def __str__(self):
		return self.post.title + ' | by:' +str(self.name)

	def get_absolute_url(self):
		return reverse('home', args=(str(self.id)))

class Profile(models.Model):
	user 			= models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	Phone 			= models.CharField(max_length=50, null=True, blank=True,)
	bio				= models.TextField()
	profile_pic	 	= models.ImageField(null=True, blank=True, upload_to='images/profile/')

	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		return reverse('home')

