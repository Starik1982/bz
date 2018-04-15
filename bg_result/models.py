
from django.db import models
from guild_members.models import GuildMembers
from django.db.models.signals import post_save
from datetime import date


# Create your models here.

class Minimum(models.Model):

	force = models.IntegerField(default = 1)
	minimum = models.IntegerField(default = 1)



class BgResult(models.Model):

	nickname = models.ForeignKey(GuildMembers, blank = True, null = True, default = None)
	result = models.IntegerField(default = 1)
	bg_date = models.DateField(auto_now_add = True, auto_now = False)
	bg_index = models.IntegerField(default = 1)
	

	
	def __str__(self):
		return "%s, %s, %s" % (self.nickname, self.result, self.bg_date)




	def save(self, *args, **kwargs):
		force_members = self.nickname.force										#сила текущего игрока
		min_result = Minimum.objects.all()
		for item in min_result:
			if force_members == item.force:
				self.bg_index = self.result - item.minimum		
	
		super(BgResult, self).save(*args, **kwargs)









	
	


	