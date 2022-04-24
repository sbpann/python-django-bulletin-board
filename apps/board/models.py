from django.db import models
from django.contrib import auth

User = auth.get_user_model()

class Board(models.Model):
    name = models.CharField(max_length=255, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    moderators = models.ManyToManyField(User, blank=True, related_name='board_moderators')

class Thread(models.Model):
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=False)
    
class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(blank=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, null=False)