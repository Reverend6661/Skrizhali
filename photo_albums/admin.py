from django.contrib import admin
from .models import Photo_album, Photo
from django.contrib.admin import TabularInline

class PhotoInline(admin.TabularInline):
    model = Photo
    felds = ('image', 'image_tag', 'is_cover')
    readonly_fields = ('image_tag',)
    extra = 3

@admin.register(Photo_album)
class Photo_albumAdmin(admin.ModelAdmin):
    inlines = [ PhotoInline, ]