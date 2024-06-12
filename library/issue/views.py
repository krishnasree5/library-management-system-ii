from django.shortcuts import render, redirect, get_object_or_404
from .forms import IssueForm, EditForm
from .models import Issue
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def new(request):

    if request.user.type == 'Staff':
        if request.method == 'POST':
            form = IssueForm(request.POST)
            if form.is_valid():
                issue = form.save(commit=False)
                issue.user = form.cleaned_data['user']
                issue.book = form.cleaned_data['book']
                issue.save()
                return redirect('issue:notifications')
        
        else:
            form = IssueForm()
        
        return render(request, 'issue/form.html', {
            'form': form,
            'title': 'New Issue'
        })
    
    else:
        return redirect('/')
    
@login_required
def edit(request, pk):

    if request.user.type == 'Staff':
        alert = get_object_or_404(Issue, pk=pk)
        if request.method == 'POST':
            form = EditForm(request.POST, instance=alert)

            if form.is_valid():
                form.save()
                return redirect('issue:notifications')
				
        else:
            form = EditForm(instance=alert)

        return render(request, 'issue/form.html', {
            'form': form,
            'title': 'Edit Issue'
        })
    
    else:
        return redirect('/')
    
@login_required
def delete(request, pk):

    if request.user.type == 'Staff':
        alert = get_object_or_404(Issue, pk=pk)
        alert.delete()
        return redirect('issue:notifications')

    else:
        return redirect('/')

@login_required
def notifications(request):
    
    if request.user.type == 'Student':
        alerts = Issue.objects.filter(Q(user=request.user) & Q(due='yes'))

    elif request.user.type == 'Staff':
        alerts = Issue.objects.filter(due='yes')

    return render(request, 'issue/notifications.html', {
        'alerts': alerts
    })
