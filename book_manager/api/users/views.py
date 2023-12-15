from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordResetView
from djoser.views import UserViewSet

from api.pagination import LimitPageNumberPagination
# from users.tasks import send_welcome_email


User = get_user_model()


class CustomDjoserUserViewSet(UserViewSet):
    pagination_class = LimitPageNumberPagination

    # def perform_create(self, serializer):
    #     username_email = serializer.save()
    #     send_welcome_email.delay(username_email)


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration / password_reset_form.html '
