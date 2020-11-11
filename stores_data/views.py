from django.shortcuts import render

from .models import User
from .forms import ParentForm,ChildForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

def home(request):
    profiles = User.objects.all()
    context = {
        'profiles': profiles,
    }
    return render(request, 'Store_Data/home.html', context)

def mainreg(request):
    return render(request, 'Store_Data/main_register.html')

def parent(request):
    parent_form = ParentForm(request.POST or None)
    if parent_form.is_valid():
        profile = parent_form.save(commit=False)
        profile.save()
        profiles = User.objects.all()
        context = {
            'profiles': profiles,
        }
        return render(request, 'Store_Data/home.html',context)
    context = {
        "parent_form": parent_form,
    }
    return render(request, 'Store_Data/parent.html', context)

def child(request):
    child_form = ChildForm(request.POST or None)
    if child_form.is_valid():
        profile = child_form.save(commit=False)
        profile.save()
        profiles = User.objects.all()
        context = {
            'profiles': profiles,
        }
        return render(request, 'Store_Data/home.html',context)
    context = {
        "child_form": child_form,
    }
    return render(request, 'Store_Data/child.html', context)

def parent_edit(request,id):
    profile = User.objects.get(pk=id)
    parent_edit = ParentForm(request.POST or None, instance=profile)
    if parent_edit.is_valid():
        profiles = User.objects.filter(pk=id).get(),
        parent_edit.save()
        context = {
            'profiles': profiles,
            'parent_edit': parent_edit,
        }
        messages.info(request, 'Information Updated')
        return render(request, 'Store_Data/parent_edit.html', context)

    profiles = User.objects.filter(pk=id).get(),
    parent_edit = ParentForm(instance=profile)

    context = {
        'profiles': profiles,
        'parent_edit': parent_edit,
    }
    print(context)

    return render(request, 'Store_Data/parent_edit.html', context)

def child_edit(request,id):
    profile = User.objects.get(pk=id)
    child_edit = ChildForm(request.POST or None, instance=profile)
    if child_edit.is_valid():
        profiles = User.objects.filter(pk=id).get(),
        child_edit.save()
        context = {
            'profiles': profiles,
            'child_edit': child_edit,
        }
        messages.info(request, 'Information Updated')
        return render(request, 'Store_Data/child_edit.html', context)

    profiles = User.objects.filter(pk=id).get(),
    child_edit = ChildForm(instance=profile)

    context = {
        'profiles': profiles,
        'child_edit': child_edit,
    }
    print(context)

    return render(request, 'Store_Data/child_edit.html', context)

def delete_user(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('store_data:home')




