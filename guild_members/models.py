from django.db import models


# Create your models here.
class GuildMembers(models.Model):

	nickname = models.CharField(max_length = 64, blank = True, null = True, default = None)
	force = models.IntegerField(default = 1)


	def __str__(self):
		return "%s, %s" % (self.nickname, self.force)
	