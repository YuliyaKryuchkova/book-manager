from rest_framework import serializers

from books.models import Book, Author, Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = (
            'name',
            'id',
        )


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = (
            'name',
            'id',
        )


class BookListSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)
    authors = AuthorSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Book
        fields = (
            'id',
            'name',
            'authors',
            'publication_date',
            'genre',
            'isbn',
        )


class BookSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)
    authors = AuthorSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Book
        fields = (
            'id',
            'name',
            'authors',
            'publication_date',
            'genre',
            'isbn',
            'time_create',
            'time_update',
        )
