from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from .serializers import GenreSerializer, AuthorSerializer, BookListSerializer, \
    BookSerializer

from books.models import Author, Book, Genre
from api.permissions import IsAuthorOrReadOnly
from api.pagination import LimitPageNumberPagination


class GenreViewSet(ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    pagination_class = LimitPageNumberPagination

    def get_queryset(self):
        ordered_queryset = super().get_queryset().order_by('name')
        return ordered_queryset


class AuthorViewSet(ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    ordered_queryset = queryset.order_by('name')
    pagination_class = LimitPageNumberPagination


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    ordered_queryset = queryset.order_by('name')
    pagination_class = LimitPageNumberPagination

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = BookSerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = BookSerializer(
            instance,
            data=request.data,
            partial=partial
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
