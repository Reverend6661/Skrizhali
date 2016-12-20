from __future__ import unicode_literals

from django.db import models

class Album(models.Model):

	name = models.CharField(max_length=75)
	release_year = models.CharField(max_length=4)
	cover = models.ImageField()
	link = models.URLField(max_length=100)
	songs_list = models.TextField()

	def __unicode__(self):
		return "{} - {}".format(self.name, self.release_year)
	class Meta:
		verbose_name = u"Альбом"
# Create your models here.
