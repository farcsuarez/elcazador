from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('countrylist/', views.countrylist, name='countrylist'),
    path('countryform', views.countryform, name='countryform'),
    path('countryform/<int:country_id>/', views.countryformUpdate, name='countryformUpdate'),
    path('bookform', views.bookform_view, name='bookform_view'),
    #path('<int:book_id>', views.detail, name='detail'),
]