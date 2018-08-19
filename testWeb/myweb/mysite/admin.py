from django.contrib import admin
from .models import Photo

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag',)

    exclude = ('image_file',)

admin.site.register(Photo, PhotoAdmin)