# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime    

from django.db import models

class Videos(models.Model):

	name = models.CharField(max_length=75)
	link = models.URLField(max_length=100)
	description = models.TextField()
	date = models.DateTimeField(default=datetime.now, blank=True)

	def __unicode__(self):
		return self.name
	
	class Meta:
		verbose_name = "Видео"
		verbose_name_plural = "Видео"



# Create your models here.
