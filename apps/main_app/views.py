from django.shortcuts import render, redirect
from models import User
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'user': User.objects.all()
    }
    return render(request, 'main_app/index.html', context)

def add(request):
    return render(request, 'main_app/create.html')

def create(request):
    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
    )
    return redirect('/')

def show(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'main_app/show.html', context)

def edit(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'main_app/edit.html', context)

def update(request, user_id):
    user_to_update = User.objects.get(id=user_id)
    user_to_update.first_name = request.POST['first_name']
    user_to_update.last_name = request.POST['last_name']
    user_to_update.email = request.POST['email']
    user_to_update.save()
    return redirect('/')

def delete(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/')