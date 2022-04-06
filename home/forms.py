from django import forms
from home.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"