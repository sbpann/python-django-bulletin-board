from apps.rest_auth.models import Token
import datetime

def Find(id):
    try:
        token = Token.objects.get(id=id)
        if datetime.datetime.now(datetime.timezone.utc) > token.expired_at:
            token.delete()
            return None
        return token
    except:
        return None