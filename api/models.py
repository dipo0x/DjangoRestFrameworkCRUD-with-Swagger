from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(blank=True, null=False)
    name = models.CharField(max_length=200, blank=True, null=False)
    image = models.FileField(upload_to='', null=False, blank=True)
    text = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=7)

    def __str__(self):
        return self.name