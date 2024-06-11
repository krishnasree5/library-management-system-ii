from django.shortcuts import render, redirect
from .forms import IssueForm
from django.contrib.auth.decorators import login_required

@login_required
def new_issue(request):
    if request.user.type == 'Staff':
        if request.method == 'POST':
            form = IssueForm(request.POST)
            if form.is_valid():
                issue = form.save(commit=False)
                issue.user = form.cleaned_data['user']
                issue.book = form.cleaned_data['book']
                issue.save()
                return render(request, 'main/home.html')
        else:
            form = IssueForm()
        
        return render(request, 'issue/form.html', {
            'form': form,
            'title': 'New Issue'
        })
    else:
        return redirect('/')