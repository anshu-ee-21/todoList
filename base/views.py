from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.contrib import messages
from .decorators import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def index(request):
    # tasks = Task.objects.all()
    tasks = request.user.task_set.all()
    context = {'tasks':tasks}
    return render(request, 'base/todoList.html', context)

@login_required(login_url='login')
def createTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'base/createTask.html', context)

@login_required(login_url='login')
def updateTask(request, pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form' : form}
    return render(request, 'base/createTask.html', context)
@login_required(login_url='login')
def deleteTask(request, pk):
    task = Task.objects.get(id = pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    context = {'item': task}
    return render(request, 'base/delete.html', context)

@login_required(login_url='login')
def completedTask(request):
    tasks = Task.objects.filter(complete = 'True')
    context = {'tasks': tasks}
    return render(request, 'base/todoList.html', context)

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user =form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+ username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'base/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect')
        
        return redirect('login')
    context = {}
    return render(request, 'base/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')