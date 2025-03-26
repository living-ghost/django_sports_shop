from django.contrib.auth.backends import BaseBackend
from .models import Register

class UserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Handle both email and username cases
        email = kwargs.get('email', username)
        
        if not email or not password:
            return None

        try:
            user = Register.objects.get(email=email)
            if user.check_password(password):
                return user
        except Register.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return Register.objects.get(pk=user_id)
        except Register.DoesNotExist:
            return None