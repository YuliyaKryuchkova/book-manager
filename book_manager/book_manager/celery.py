# import os
#
# from celery import Celery
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_manager.settings')
#
# app = Celery('book_manager')
#
#
# app.config_from_object('django.conf:settings', namespace='CELERY')
#
# app.autodiscover_tasks()
#
#
# # @app.task(bind=True, ignore_result=True)
# # def debug_task(self):
# #     print(f'Request: {self.request!r}')
#
# app.conf.beat_schedule = {
#     'creating_message': {
#         'task': 'users.tasks.send_welcome_email',
#         'schedule': 15.0
#     }
# }
