from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('bookform', views.bookform_view, name='bookform_view'),
    path('countryform', views.countryform, name='countryform'),
    path('countryform/<int:country_id>/', views.countryformUpdate, name='countryformUpdate'),
    #path('<int:book_id>', views.detail, name='detail'),
]