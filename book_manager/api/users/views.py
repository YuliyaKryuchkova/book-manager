from django.contrib.auth import get_user_model
from djoser.views import UserViewSet

from api.pagination import LimitPageNumberPagination
from users.tasks import send_welcome_email


User = get_user_model()


class CustomDjoserUserViewSet(UserViewSet):
    pagination_class = LimitPageNumberPagination

    def perform_create(self, serializer):
        username_email = serializer.save()
        send_welcome_email.delay(username_email)

    # def send_email(self):
    #     send_feedback_email_task.delay(
    #         self.cleaned_data["email"], self.cleaned_data["message"]
    #     )
