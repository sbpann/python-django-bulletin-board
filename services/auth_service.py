from django.contrib import auth
from . import jwt_service 
import datetime
User = auth.get_user_model()

def Login(username, password):
    try:
        user = User.objects.get(username=username)
    except:
        return None
    if user.check_password(password):
        return jwt_service.Encode({"user_id": user.id, "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=30)})
    return None
