from django.contrib import admin

from .models import Author, Book, Genre, AuthorsBook


class AuthorsBookInline(admin.TabularInline):
    model = AuthorsBook
    min_num = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [AuthorsBookInline]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    model = Author


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    model = Genre
