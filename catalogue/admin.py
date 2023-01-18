from django.contrib import admin

from catalogue.models import Book, Author, Genre, BookInstance


# admin.site.register(Book)
class BookInline(admin.TabularInline):
    model = Book
@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

class BookInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    model = BookInstance


list_filter = ('status', 'due_back')

fieldsets = (
    (None, {
        'fields': ('book', 'imprint', 'id')
    }),
    ('Availability', {
        'fields': ('status', 'due_back')
    }),
)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
