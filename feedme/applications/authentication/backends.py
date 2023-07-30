from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models import Q
from applications.user_handler.models import User as UserModel


# UserModel = get_user_model()

class EmailOrPhoneAuthentication(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):        
        if username is None:
            return None
        
        user = UserModel.customer.get(Q(email=username) | Q(phone=username))

        if user and user.check_password(password):
            return user
        
        return None

    def get_user(self, id):
        try:
            return UserModel.customer.get(pk= id)
        except UserModel.DoesNotExist:
            return None
        