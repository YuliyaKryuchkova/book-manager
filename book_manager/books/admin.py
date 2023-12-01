from django.contrib import admin

from .models import Author, Book, Genre


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'author',
        'publication_date',
        'isbn',
        'genre',
    )
    search_fields = (
        'id',
        'name',
        'author',
        'publication_date',
        'isbn',
        'genre',
    )
    list_filter = (
        'name',
        'author',
    )
    empty_value_display = '-пусто-'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    search_fields = (
        'id',
        'name',
    )
    list_filter = (
        'name',
    )
    empty_value_display = '-пусто-'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    search_fields = (
        'id',
        'name',
    )
    list_filter = (
        'name',
    )
    empty_value_display = '-пусто-'
