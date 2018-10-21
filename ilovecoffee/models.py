from django.db import models
from django.utils import timezone


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    no_of_coffee = models.CharField(max_length=5)
    location = models.TextField()
    is_canceled = models.BooleanField(default=False)
    create_at = models.DateTimeField(default=timezone.now)

    def pusblish(self):
        self.save()

    def __str__(self):
        return self.location
