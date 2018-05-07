from django.db import models
from ckeditor.fields import RichTextField


class News(models.Model):

	title = models.CharField(max_length = 64, blank = True, null = True, default = None)
	preview_news = models.TextField(max_length = 220, blank = True, null = True, default = None)
	news = RichTextField(blank = True, null = True, default = None)
	date = models.DateTimeField(auto_now_add = True, auto_now = False)
	
	def __str__(self):
		return "%s, %s" % (self.title, self.date)




class Video(models.Model):
	title = models.CharField(max_length = 64, blank = True, null = True, default = None)
	preview_video = models.TextField(max_length = 500, blank = True, null = True, default = None)
	video = models.TextField(max_length = 500, blank = True, null = True, default = None)
	date = models.DateTimeField(auto_now_add = True, auto_now = False)

	def __str__(self):
		return "%s, %s, %s" % (self.title, self.video, self.date)

class Ads(models.Model):
	ads = RichTextField(blank = True, null = True, default = None)
	date = models.DateTimeField(auto_now_add = True, auto_now = False)
	def __str__(self):
		return "%s" % (self.ads)

class Faq(models.Model):

	title = models.CharField(max_length = 200, blank = True, null = True, default = None)
	faq = RichTextField(blank = True, null = True, default = None)
	
	
	def __str__(self):
		return "%s, %s" % (self.title, self.faq)


class Hiro(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	image = models.ImageField(upload_to='images/')
	
	def __str__(self):
		return "%s, %s" % (self.name, self.image)