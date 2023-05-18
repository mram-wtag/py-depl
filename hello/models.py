from django.db import models


# Create your models here.

class SayHello(models.Model):
    say = models.CharField(max_length=200)

    def __str__(self):
        return self.say
