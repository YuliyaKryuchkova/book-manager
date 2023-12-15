# from django.contrib.auth import get_user_model
# from celery import shared_task
# from django.core.mail import send_mail
#
# from book_manager.settings import EMAIL_HOST_USER, EMAIL_DOMAIN
#
# User = get_user_model()


# @shared_task
# def send_welcome_email(username_email):
#     subject = 'Добро пожаловать!'
#     message = 'Приветствуем вас на нашем сайте.'
#     from_email = f"{EMAIL_HOST_USER}@{EMAIL_DOMAIN}"
#     recipient_list = [username_email]
#     send_mail(subject, message, from_email, recipient_list)

# @shared_task
# def send_welcome_email():
#     send_mail(
#         'Приветствуем вас на нашем сайте',
#         f"{EMAIL_HOST_USER}@{EMAIL_DOMAIN}",
#         [f"{EMAIL_HOST_USER}@{EMAIL_DOMAIN}"]
#     )


# @shared_task()
# def send_feedback_email_task(email_address, message):
#     """Sends an email when the feedback form has been submitted."""
#     sleep(20)  # Simulate expensive operation(s) that freeze Django
#     send_mail(
#         "Your Feedback",
#         f"\t{message}\n\nThank you!",
#         "support@example.com",
#         [email_address],
#         fail_silently=False,
#     )
