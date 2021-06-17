from django.shortcuts import render,redirect
from .models import Task
from .form import UserForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(response):
    content = {"response":response}
    return render(response,"home.html",content)

@login_required(login_url='/login')
def tasks(response):
    if response.method == "POST":
        
        if response.POST.get("submit"): 
            name = response.POST.get('title')
            about = response.POST.get('description')

            t = Task(name=name, about=about)
            t.save()
            response.user.task.add(t)
        
        elif response.POST.get("delete"):
            id = int(response.POST.get("delete"))
            t = response.user.task.get(id=id)
            t.delete()

    lists = response.user.task.all()
    content = {"lists":lists, "response": response}
    return render(response,"tasks.html",content)

@login_required(login_url='/login')
def items(response, id):
    try:
        t = response.user.task.get(id=id)
    except Exception as e:
        return redirect('/tasks')

    if response.method == "POST":

        if response.POST.get("submit"):
            description = response.POST.get("description")
            t.item_set.create(description=description)
        
        elif response.POST.get("in-process"):
            item = t.item_set.get(id=int(response.POST.get("in-process")))
            item.processing = True
            item.save()
        elif response.POST.get("complete"):
            item = t.item_set.get(id=int(response.POST.get("complete")))
            item.complete = True
            item.save()    

        elif response.POST.get("delete"):
            item = t.item_set.get(id=int(response.POST.get("delete")))
            item.delete()

    lists = t.item_set.all()
    content = {"items":lists, "task":t, "response": response}
    return render(response,"items.html",content)

def about(response):
    content = {}
    return render(response,"about.html",content)

def loginpage(response):

    if response.user.is_authenticated:
        return redirect("/")
    
    else:

        if response.method == "POST":
            username = response.POST.get("username")
            password = response.POST.get("password")
            user = authenticate(response, username=username,password=password)

            if user is not None:
                login(response,user)
                return redirect("/")

            else:
                messages.error(response,"Username OR Password is invalid")
                return redirect("/login")

        content = {}
        return render(response,"login.html",content)

def register(response):
    
    if response.user.is_authenticated:
        return redirect("/")
    
    else:
    
        form = UserForm()
        
        if response.method == "POST":
            form = UserForm(response.POST)
            if form.is_valid():
                form.save()
                messages.success(response,"Registered successfully, Please login.")
                return redirect('/login')

        content = {"form":form}
        return render(response,"register.html",content)

def logoutpage(response):
    logout(response)
    return redirect("/login")