from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from .serializers import GenreSerializer, AuthorSerializer, BookListSerializer, \
    BookSerializer

from books.models import Author, Book, Genre


class GenreViewSet(ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class AuthorViewSet(ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BookSerializer
        return self.serializer_class
