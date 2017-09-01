from django.db import models

# Create your models here.
class Stream(models.Model):

    name = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    live = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.name)

    