# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce import models as tinymce_models


class News(models.Model):

	header = models.CharField(max_length=75)
	content = models.TextField(blank=True)
	created_date = models.DateTimeField(blank=True, null=True)
	image = models.ImageField(blank = True, upload_to = 'albums/static')

	def __unicode__(self):
		return self.header

	class Meta:
		verbose_name = 'Новости'
		verbose_name_plural = 'Новости'
		ordering = ['-created_date']

# Create your models here.
