from django.shortcuts import render, redirect
from .forms import IssueForm

def new_issue(request):
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
