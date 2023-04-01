from django.db import models
from django.contrib.auth.models import User


class Followers(models.Model):
    """
    Followers model
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')
    created_date = models.DateTimeField(auto_now_add=True)
    followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followed')

    class Meta:
        ordering = ['-created_date']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f"{self.owner} {self.followed}"
