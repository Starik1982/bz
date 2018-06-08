from django.db import models
from django.contrib.auth.models import User
from guild_members.models import GuildMembers
from django.utils import timezone


class PersonalRoom(models.Model):
	avatar = models.ImageField(upload_to='images/', blank = True, null = True, default = None)
	name = models.CharField(max_length = 200, blank = True, null = True, default = None)
	sername = models.CharField(max_length = 200, blank = True, null = True, default = None)
	yourself = models.TextField( blank = True, null = True, default = None)
	user = models.OneToOneField(User, blank = True, null = True, default = None)
	gild_mamber = models.OneToOneField(GuildMembers, blank = True, null = True, default = None)
	date_of_entry = models.DateField(default=timezone.now, auto_now = False)
	vkurls = models.CharField(max_length = 200, blank = True, null = True, default = None)
	fburls = models.CharField(max_length = 200, blank = True, null = True, default = None)
	insturls = models.CharField(max_length = 200, blank = True, null = True, default = None)


