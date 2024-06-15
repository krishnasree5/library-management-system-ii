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
    alerts = Issue.objects.filter(due='yes')
    
    query = request.GET.get('query', '')
    if query:
        alerts = alerts.filter(Q(user__username__icontains=query) | Q(book__title__icontains=query))

    if request.user.type == 'Non-staff':
        alerts = alerts.filter(Q(user=request.user))

    return render(request, 'issue/notifications.html', {
        'query': query,
        'alerts': alerts
    })
