from django import forms
from .models import Book, Country

# creating forms

class CountryForm(forms.ModelForm):
	class Meta:
		model = Country
		fields = "__all__"
      
class DatosForm(forms.Form):

	first_name = forms.CharField(max_length = 200)
	last_name = forms.CharField(max_length = 200)
	roll_number = forms.IntegerField(
					help_text = "Enter 6 digit roll number"
					)
	password = forms.CharField(widget = forms.PasswordInput())


class BooksForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"