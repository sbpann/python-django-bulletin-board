from django.contrib import auth
User = auth.get_user_model()

def Find(id):
    try:
        return User.objects.get(id=id)
    except:
        return None
