

def get_user_username(request):
    if  request.user.is_authenticated:
        return {"get_username": request.user.username}
    return {"get_username": "unauthorized"}

