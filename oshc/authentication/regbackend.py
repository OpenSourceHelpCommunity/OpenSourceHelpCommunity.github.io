from django.contrib.auth import get_user_model


class EmailLoginBackend(object):
    '''
    This class checks that the user can be authenticated via our backend and
    if it fails than normal authentication backend is used.
    '''

    def authenticate(self, username=None, password=None):
        user_cls = get_user_model()
        try:
            user = user_cls.objects.get(email=username)
            if user.check_password(password):
                return user
        except user_cls.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        user_cls = get_user_model()
        try:
            return user_cls.objects.get(pk=user_id)
        except user_cls.DoesNotExist:
            return None
