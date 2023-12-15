from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .books.views import GenreViewSet, AuthorViewSet, BookViewSet
from .users.views import CustomDjoserUserViewSet, CustomPasswordResetView

app_name = 'api'

router = DefaultRouter()

router.register(
    'books',
    BookViewSet,
    basename='books'
)
router.register(
    'books',
    BookViewSet,
    basename='books'
)
router.register(
    'users',
    CustomDjoserUserViewSet,
    basename='users'
)
router.register(
    'genres',
    GenreViewSet,
    basename='genres'
)
router.register(
    'authors',
    AuthorViewSet,
    basename='authors'
)

urlpatterns = [
    path(
        '',
        include(router.urls)
    ),
    path(
        'auth/',
        include('djoser.urls.authtoken')
    ),
    path('users/reset-password/',
         CustomPasswordResetView.as_view(),
         name='password_reset'),
]
