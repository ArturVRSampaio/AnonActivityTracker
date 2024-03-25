from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from app.forms import NewGroup, NewEntry, NewActivityType
from app.models import Group, ActivityType, Entry


def index(request):
    return render(request, 'index.html')


@login_required
def groups(request):
    user = request.user
    return render(request, 'groups.html', {'user': user})


@login_required
def group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    is_owner = group.owners.filter(id=request.user.id).exists()
    if not is_owner:
        return redirect('groups')
    return render(request, 'group.html', {'group': group})

@login_required
def new_group(request):
    if request.method == 'POST':
        form = NewGroup(request.POST)
        if form.is_valid():
            group: Group = Group()
            group.name = form.cleaned_data['name']
            group.description = form.cleaned_data['description']
            group.save()
            group.owners.add(request.user)
            group.save()

            return redirect('group', group_id=group.id)

    form = NewGroup()
    return render(request, 'newGroup.html', {'form': form})


@login_required
def new_entry(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    is_owner = group.owners.filter(id=request.user.id).exists()
    if not is_owner:
        return redirect('groups')

    if request.method == 'POST':
        form = NewEntry(request.POST)
        if form.is_valid():
            entry = Entry()
            entry.activityType = form.cleaned_data['activityType']
            entry.group = group
            entry.text = form.cleaned_data['text']
            entry.user = request.user
            entry.save()

            return redirect('group', group_id=group.id)

    form = NewEntry()
    return render(request, 'newEntry.html', {'form': form})


@login_required
def new_activity_type(request):
    if request.method == 'POST':
        form = NewActivityType(request.POST)
        if form.is_valid():
            activity = ActivityType()
            activity.name = form.cleaned_data['name']
            activity.save()

            return redirect('groups')

    form = NewActivityType()
    return render(request, 'newActivityType.html', {'form': form})
