from django.shortcuts import  get_object_or_404
from .models import Book
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from django.contrib.auth import logout
from .forms import UserForm
from django.views.generic.edit import CreateView

class IndexView(generic.ListView):
    template_name =  'book/index.html'
    context_object_name = 'all_books'

    def get_queryset(self):
        return Book.objects.all()


def detail(request, book_isbn):
    book = get_object_or_404(Book,pk = book_isbn)
    return render(request, 'book/detail.html', {'book': book})


def favorite(request, book_isbn):
    book = Book.objects.get(isbn=book_isbn)
    book.favorite = True
    book.save()
    return render(request, 'book/detail.html', {'book': book, })


def unfav(request, book_isbn):
    book = Book.objects.get(isbn=book_isbn)
    book.favorite = False
    book.save()
    return render(request, 'book/detail.html', {'book': book, })


class BookCreate(CreateView):
    model = Book
    fields = ['isbn','logo','title','author','desc']


class UserFormView(View):
    form_class = UserForm
    template_name = 'book/register_form.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username = username, password = password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('book:index')

        return render(request, self.template_name, {'form': form})

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'book/login.html')
    else:
        book = Book.objects.filter(user=request.user)
        query = request.GET.get("q")
        if query:
            return render(request, 'book/index.html', {
                'book': book,

            })
        else:
            return render(request, 'book/index.html', {'book': book})

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'book/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                book = Book.objects.all()
                return render(request, 'book/index.html', {'book': book})
            else:
                return render(request, 'book/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'book/login.html', {'error_message': 'Invalid login'})
    return render(request, 'book/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                book = Book.objects.filter(user=request.user)
                return render(request, 'book/index.html', {'book': book})
    context = {
        "form": form,
    }
    return render(request, 'book/register_form.html', context)
