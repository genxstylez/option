from django.db import models
from django.utils.translation import ugettext_lazy as _

class About(models.Model):
    def about_path(self, filename):
        return 'about/about.%s' % filename.split('.')[1]
    content = models.TextField(_('content'))
