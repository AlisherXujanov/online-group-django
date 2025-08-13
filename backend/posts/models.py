from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # CASCADE  => delete post if the user is deleted
    # PREVENT  => prevent post from being deleted if the user is deleted
    # SET_NULL => set the post to null if the user is deleted