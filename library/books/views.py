from django.shortcuts import render

# Create your views here.
def Test(request):
    return render(request, 'test.html')