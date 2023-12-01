from django.db import models


class Book(models.Model):
    name = models.CharField(
        'Название книги',
        max_length=150,
    )
    author = models.ForeignKey(
        'Author',
        on_delete=models.SET_NULL,
        null=True)
    publication_date = models.DateField()
    isbn = models.CharField(
        'ISBN',
        max_length=13,
        help_text='13 символов <a href="https://www.isbn-international.org/content/what-isbn">ISBN номера</a> книги',
    )
    genre = models.ForeignKey(
        'Genre',
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(
        max_length=150,
    )

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=150,
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name
