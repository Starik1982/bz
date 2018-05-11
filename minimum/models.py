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
	image = models.ImageField(upload_to='images/', blank = True, null = True, default = None)
	image_evolution = models.ImageField(upload_to='images/', blank = True, null = True, default = None)
	image_skill = models.ImageField(upload_to='images/', blank = True, null = True, default = None)
	hp = models.IntegerField(default=0)
	hp_evolution_1 = models.IntegerField(default=0)
	hp_evolution_2 = models.IntegerField(default=0)
	attack = models.IntegerField(default=0)
	attack_evolution_1 = models.IntegerField(default=0)
	attack_evolution_2 = models.IntegerField(default=0)
	attack_speed = models.IntegerField(default=0)
	running_speed = models.IntegerField(default=0)
	running_speed_1 = models.IntegerField(default=0)
	running_speed_2 = models.IntegerField(default=0)
	attack_radius = models.IntegerField(default=0)
	accuracy = models.IntegerField(default=0)
	accuracy_1 = models.IntegerField(default=0)
	accuracy_2 = models.IntegerField(default=0)
	evasion = models.IntegerField(default=0)
	critical_hit = models.IntegerField(default=0)
	critical_damage = models.IntegerField(default=0)
	critical_damage_1 = models.IntegerField(default=0)
	critical_damage_2 = models.IntegerField(default=0)
	critical_resistance = models.IntegerField(default=0)
	skill_1 = models.TextField( blank = True, null = True, default = None)
	skill_2 = models.TextField( blank = True, null = True, default = None)
	skill_3 = models.TextField( blank = True, null = True, default = None)
	skill_4 = models.TextField( blank = True, null = True, default = None)
	skill_5 = models.TextField( blank = True, null = True, default = None)
	skill_6 = models.TextField( blank = True, null = True, default = None)
	skill_7 = models.TextField( blank = True, null = True, default = None)
	skill_8 = models.TextField( blank = True, null = True, default = None)
	skill_9 = models.TextField( blank = True, null = True, default = None)
	skill_10 = models.TextField( blank = True, null = True, default = None)
	skill_11 = models.TextField( blank = True, null = True, default = None)
	skill_12 = models.TextField( blank = True, null = True, default = None)

