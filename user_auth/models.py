from django.db import models
from django.contrib.auth.models import User


genders = (
    ('female', 'Female'),
    ('male', 'Male'),
)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users_photo/')
    bio = models.TextField()
    gender = models.CharField(max_length=6, choices=genders)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username



class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.message