# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.sites.models import Site

from django.db import models

class Photo_album(models.Model):

	name = models.CharField('Имя альбома', max_length=75)
	date = models.DateTimeField('Дата', blank=True, null=True)

	def __unicode__(self):
		return self.name

	def cover(self):
		for i in Photo.objects.filter(photo_album=self):
			if i.is_cover:
				return i
				break

	
	class Meta:
		verbose_name = "Фотоальбом"
		verbose_name_plural = "Фотоальбомы"

class Photo(models.Model):

	name = models.CharField('Имя', max_length=75, default="Фотография без названия")
	photo_album = models.ForeignKey(Photo_album, related_name='photos')
	image = models.ImageField('Фотография', upload_to = 'photo_albums/photos')
	is_cover = models.BooleanField('Обложка фотоальбома', default=False)


	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = "Фотография"
		verbose_name_plural = "Фотографии"



	def image_tag(self):
		image = self.image.url
		current_site = Site.objects.get_current()
		domain = current_site.domain
		return u'<img src="{}static/{}" width=20%>'.format(domain, image)


	image_tag.short_description = 'Предпросмотр'
	image_tag.allow_tags = True

# Create your models here.
