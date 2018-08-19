from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Photo(models.Model):
    image = models.ImageField(upload_to='', max_length=100)

    def image_tag(self):
        return u'<img src="%s" width="200px" />' % self.img_file.url
    
    image_tag.short_description = _('image')
    image_tag.allow_tags = True