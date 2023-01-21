from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.views import generic

from catalogue.models import Book, BookInstance, Author, Genre


@login_required
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.all().count()
    num_genres_available = Genre.objects.filter(name__icontains='f').count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_genres_available': num_genres_available,
        'num_visits': num_visits
    }

    return render(request, 'catalogue/index.html', context=context)


# @login_required
class BookListView(generic.ListView):
    model = Book
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(BookListView, self) \
            .get_context_data(**kwargs)

        context['some_data'] = 'This is just some data'

        return context


# @login_required
class BookDetailView(generic.DetailView):
    model = Book


# @login_required
def book_detail_view(request, primary_key):
    try:
        book = Book.objects.get(pk=primary_key)
    except Book.DoesNotExist:
        raise Http404('Book does not exist')
    return render(request, 'catalogue/book_detail.html', context={'book': book})


# @login_required
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self) \
            .get_context_data(**kwargs)

        context['some_data'] = 'This is just some data'

        return context


@login_required
def author_detail_view(request, primary_key):
    try:
        author = Author.objects.get(pk=primary_key)
    except Author.DoesNotExist:
        raise Http404('Author does not exist')
    return render(request, 'catalogue/author_detail.html', context={'author': author})



class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalogue/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
