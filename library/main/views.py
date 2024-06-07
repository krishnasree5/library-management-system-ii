from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.views import LoginView


# Create your views here.
def index(request):
    return render(request, 'main/home.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = SignUpForm()

    return render(request, 'main/register.html', {
		'form': form,
	})

class CustomLoginView(LoginView):
    template_name = 'main/login.html'
