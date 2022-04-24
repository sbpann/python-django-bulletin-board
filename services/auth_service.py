import uuid
from django.contrib import auth
from apps.rest_auth.models import Token
from . import jwt_service 
import datetime

User = auth.get_user_model()

def Login(user):

    if user is None:
        return None
    payload = {
            "user_id": user.id,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours=8),
            "jti": str(uuid.uuid4())
            }
    token = Token.objects.create(id=payload.get("jti"), expired_at=payload.get("exp"), user_id=user.id)
    token.save()
    return jwt_service.Encode(payload)
