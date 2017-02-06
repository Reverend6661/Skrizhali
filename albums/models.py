# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce import models as tinymce_models


class Album(models.Model):

	name = models.CharField('Название альбома', max_length=75)
	release_year = models.CharField('Год выпуска', max_length=4)
	cover = models.ImageField('Обложка', upload_to = 'albums/static')
	link = models.URLField('Ссылка на альбом', max_length=100)
	songs_list = tinymce_models.HTMLField("Список песен", blank=True)

	def __unicode__(self):
		return "{} - {}".format(self.name, self.release_year)
	
	class Meta:
		verbose_name = "Альбом"
		verbose_name_plural = "Альбомы"

# Create your models here.
