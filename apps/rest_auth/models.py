from django.db import models
from django.contrib import auth
import uuid
User = auth.get_user_model()

class Token(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    expired_at = models.DateTimeField()
