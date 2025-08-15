from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostsForm

# CRUD  =>  Create, Read, Update, Delete

def home(request):
    context = {
        "title": "Home",
        "content": "This is the home page",
        "posts": Posts.objects.all()
    }
    return render(request, "home.html", context)

def create_post(request):
    if request.method == "POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("home")
    
    context = {
        "form": PostsForm()
    }
    return render(request, "create_post.html", context)


def update_post(request, pk:int):
    post = Posts.objects.get(pk=pk)
    
    if request.method == "POST":
        form = PostsForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect("home")
    
    context = {
        "form": PostsForm(instance=post)
    }
    return render(request, "update_post.html", context)


def delete_post(request, pk:int):
    post = Posts.objects.get(pk=pk)
    post.delete()
    return redirect("home")
    


# https://www.domain-name.com        =>  landing page
# https://www.domain-name.com/path   =>  spacial page

# PATH EX:  videos/cartoons/1
#           subjects/languages/english/a1-c2/spaking/1

# SCENARIO WITH USER
# 1. The user enters url to the browser and visits the site
# 2. The request comes to django and URLS.PY recieves it
# 3. URLS.PY checks the path and correctly identifies the view function
# 4. URLS.py passes the request to the fn and VIEWS.PY's fn creates 
#                                           a logical-response
# 5. The response is sent back to the user's browser