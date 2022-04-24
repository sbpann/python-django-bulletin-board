import uuid
from django.contrib import auth
from apps.rest_auth.models import Token
from . import jwt_service 
import datetime

User = auth.get_user_model()

def Login(username, password):
    try:
        user = User.objects.get(username=username)
    except:
        return None
    if user.check_password(password):
        payload = {
            "user_id": user.id,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=30),
            "jti": str(uuid.uuid4())
            }
        token = Token.objects.create(id=payload.get("jti"), expired_at=payload.get("exp"), user_id=user.id)
        token
        return jwt_service.Encode(payload)
    return None
