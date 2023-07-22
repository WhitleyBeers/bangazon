from bangazonapi.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check_user(request):
    """checks to see if User has associated account"""
    uid = request.data['uid']
    user = User.objects.filter(uid=uid).first()
    
    if user is not None:
        data = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'uid': user.uid,
            'registered_on': user.registered_on,
            'profile_image_url': user.profile_image_url,
            'username': user.username
        }
        return Response(data)
    else:
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    """handles the creation of a new user for authentication"""
    user = User.objects.create(
        first_name = request.data["firstName"],
        last_name = request.data["lastName"],
        email = request.data["email"],
        uid = request.data["uid"],
        profile_image_url = request.data["profileImageUrl"],
        username = request.data["username"],
    )
    
    data = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'uid': user.uid,
        'registered_on': user.registered_on,
        'profile_image_url': user.profile_image_url,
        'username': user.username
    }
    return Response(data)
