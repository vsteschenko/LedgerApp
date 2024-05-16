from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .categories import categories

class Transaction(models.Model):
    transaction = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField(default=0)
    category = models.CharField(max_length=100, choices=categories)
    place = models.CharField(max_length=100, default='')
    comment = models.CharField(max_length=100, default='')
