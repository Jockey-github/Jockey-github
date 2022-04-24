from django.db import models

# Create your models here.
# from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Mock(models.Model):
    mock_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.mock_name