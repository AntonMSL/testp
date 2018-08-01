from django.db import models
from django.utils import timezone
# Create your models here.

class Ticket(models.Model):
    fio = models.CharField(max_length=200)
    age = models.DateTimeField(
            default=timezone.now)
    problem = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)




    def __str__(self):
        return self.fio