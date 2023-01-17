from django.contrib import admin

from catalogue.models import Book, Author, Genre, BookInstance

admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
