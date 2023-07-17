from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models import Q


UserModel = get_user_model()

class EmailOrPhoneAuthentication(BaseBackend):
    def authenticate(self, username=None, password=None, phone=None, **kwargs):
        valid = False
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        
        if username is None and phone is None:
            raise ValidationError("Either email or phone must be provided.")

        try:
            from django.conf import settings
            auth_settings = settings.AUTHENTICATION_FIELDS
        except AttributeError:
            return None

        auth_fields = auth_settings.get('auth_fields', None)


        q_object = None
        first_iteration = True
        for field in auth_fields:
            field_ = {f'{field}__iexact': username}

            if first_iteration:
                q_object = Q(**field_)
                first_iteration = False
            else:
                q_object |= Q(**field_)

        try:
            user = UserModel._default_manager.get(q_object)

            if valid:
                return user
            return None
        
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def get_user(self, id):
        try:
            return User.objects.get(pk= id)
        except User.DoesNotExist:
            return None


    def get_user(self, id):
        try:
            return User.objects.get(pk= id)
        except User.DoesNotExist:
            return None
        