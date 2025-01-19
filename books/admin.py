from django.contrib import admin
from .models import Book, Country, Author, Editor, Genre 
# Register your models here.
admin.site.register(Book)
admin.site.register(Country)
admin.site.register(Author)
admin.site.register(Editor)
admin.site.register(Genre)