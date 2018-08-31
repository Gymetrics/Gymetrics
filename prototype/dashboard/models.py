from django.db import models

# Create your models here.
class Gym(models.Model):

    location_name = models.CharField(max_length=250)
    number_of_people = models.IntegerField()
    capacity = models.IntegerField()
    image = models.CharField(max_length=250)

    def __str__(self):
        return "{}".format(self.location_name)
    