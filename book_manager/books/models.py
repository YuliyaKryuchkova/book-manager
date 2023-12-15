from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(
        max_length=150,
        db_index=True
    )

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(
        'Название книги',
        max_length=150,
    )
    authors = models.ManyToManyField(
        Author,
        through='AuthorsBook',
        related_name='books',
        verbose_name='Авторы',
    )
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
    time_create = models.DateTimeField(
        'Дата добавления книги',
        default=timezone.now,
        db_index=True
    )
    time_update = models.DateTimeField(
        'Дата обновления информации о книге',
        auto_now=True,
        db_index=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name


class AuthorsBook(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name='Книга')

    class Meta:
        verbose_name = 'Авторы книги'
        verbose_name_plural = 'Авторы книг'

    def __str__(self):
        return f'{self.author} {self.book}'


class Genre(models.Model):
    name = models.CharField(
        max_length=150,
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        existing_genre = Genre.objects.filter(name=self.name)
        if existing_genre.exists():
            raise ValidationError('Такой жанр уже существует')
        super(Genre, self).save(*args, **kwargs)