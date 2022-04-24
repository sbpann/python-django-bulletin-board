from django.conf import settings
import jwt

def Encode(payload):
    if not isinstance(payload, dict):
        payload = {}
    return jwt.encode(payload, settings.JWT_HS256_SECRET_KEY, algorithm="HS256")

def Decode(token):
    try:
        return True, jwt.encode(token, settings.JWT_HS256_SECRET_KEY, algorithm="HS256")
    except:
        return False, None