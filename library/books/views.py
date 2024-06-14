from django.shortcuts import render
from .models import Book, Category
from django.db.models import Q

# Create your views here.

def search(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    books = Book.objects.all()
    categories = Category.objects.all()

    if category_id:
        books = books.filter(category=category_id)    
    if query:
        books = books.filter(Q(title__icontains=query)|Q(isbn__icontains=query)|Q(author__icontains=query)|Q(publisher__icontains=query))
    else:
        books = books[:9]

    return render(request, 'books/search.html', {
        'books': books,
        'categories': categories,
        'query': query,
        'category_id': int(category_id)
    })


def detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'books/detail.html',{
        'book': book,
    })