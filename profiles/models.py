from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    bio = models.CharField(max_length=255, blank=True, default='')
    address = models.CharField(max_length=127, blank=True, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    def __repr__(self):
        return self.user.username