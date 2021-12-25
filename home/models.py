from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    desc = models.TextField()
    date = models.DateField()

    # this is for see the name of the person who contact us exp is here name
    def __str__(self):
        return self.name
