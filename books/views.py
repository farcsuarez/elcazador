from django.http import HttpResponseNotFound
from django.shortcuts import render

from books.forms import BooksForm, CountryForm



from .models import Book, Country

def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def bookform_view(request):
    context = {}
    form = BooksForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "books/datos.html", context)

def countryform(request):
    context = {}
    form = CountryForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "books/datos.html", context)

# books/views.py
def countryformUpdate(request, country_id):
    context = {}
    try:
        country = Country.objects.get(id=country_id)
        form = CountryForm(request.POST or None, instance=country)
        if form.is_valid():
            form.save()

        context['form'] = form
        return render(request, "books/datos.html", context)
    except Country.DoesNotExist:
        # Handle the case when the country with the given ID does not exist
        return HttpResponseNotFound("Country not found")