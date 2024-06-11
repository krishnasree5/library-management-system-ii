from .models import Issue
from main.models import CustomUser
from books.models import Book
from django import forms

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('username', 'book_title', 'Due')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Username'
    }))

    book_title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Book Title'
    }))

    Due = forms.ChoiceField(widget=forms.RadioSelect, choices=Issue.STATUS_CHOICES)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        book_title = cleaned_data.get('book_title')
        book_title = book_title

        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            raise forms.ValidationError(f"No user found with username: {username}")

        try:
            book = Book.objects.get(title__iexact=book_title)
        except Book.DoesNotExist:
            raise forms.ValidationError(f"No book found with title: {book_title}")

        cleaned_data['user'] = user
        cleaned_data['book'] = book
        return cleaned_data