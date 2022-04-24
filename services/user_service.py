from django.contrib import auth
User = auth.get_user_model()

def Find(id):
    try:
        return User.objects.get(id=id)
    except:
        return None

def FindByUsername(username):
    try:
        return User.objects.get(username=username)
    except:
        return None

def ValidatePassword(user, password):
    if user is None:
        return False
    return user.check_password(password)