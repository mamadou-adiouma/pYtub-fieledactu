from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Messages(models.Model):
    objects = None
    contents = models.CharField(max_length=1000)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    reponse_to = models.ForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True
    )
