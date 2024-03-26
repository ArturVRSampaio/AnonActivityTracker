import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from app.forms import NewGroup, NewEntry, NewActivityType, JoinGroupForm
from app.models import Group, ActivityType, Entry
from app.utils import get_s3_client
import uuid


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
        form = NewEntry(request.POST, request.FILES, group=group)
        if form.is_valid():
            image_file = request.FILES.get('image')
            entry = form.save(commit=False)
            entry.group = group
            entry.user = request.user

            if image_file:
                try:
                    unique_filename = f"{uuid.uuid4()}{os.path.splitext(image_file.name)[1]}"

                    s3 = get_s3_client()
                    s3.upload_fileobj(image_file, 'anontracker', unique_filename, ExtraArgs={'ACL': 'public-read'})

                    entry_url = f"https://anontracker.nyc3.digitaloceanspaces.com/anontracker/{unique_filename}"
                    entry.image_url = entry_url  # Set the image URL
                except Exception as e:
                    return redirect('new_entry', group_id=group_id)

            entry.save()
            return redirect('group', group_id=group.id)
    else:
        form = NewEntry(group=group)

    return render(request, 'newEntry.html', {'form': form})


@login_required
def new_activity_type(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    is_owner = group.owners.filter(id=request.user.id).exists()
    if not is_owner:
        return redirect('groups')

    if request.method == 'POST':
        form = NewActivityType(request.POST)
        if form.is_valid():
            activity = ActivityType()
            activity.name = form.cleaned_data['name']
            activity.group = group
            activity.save()

            return redirect('groups')

    form = NewActivityType()
    return render(request, 'newActivityType.html', {'form': form})


@login_required
def join_group(request):
    if request.method == 'POST':
        form = JoinGroupForm(request.POST)
        if form.is_valid():
            group_id = form.cleaned_data['group_id']
            group = get_object_or_404(Group, id=group_id)
            group.owners.add(request.user)
            return redirect('group', group_id=group_id)
    else:
        form = JoinGroupForm()
    return render(request, 'join_group.html', {'form': form})
