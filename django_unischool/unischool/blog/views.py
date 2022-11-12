from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from .models import Blog

# Create your views here.
def index(request):
    blog_info = Blog.objects.all()
    return render(request, "main.html", {"blog_info": blog_info})


def index_2(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"Новая лоховская страница под номером {catid}")
    

def arcvive(request, year):
    if int(year) > 2020:
        return redirect("home", permanent=True)
    return HttpResponse(f"Какой то текст + название года {year}")









def create(request):
    if request.method =="POST":
        blog = Blog()
        blog.title = request.POST.get("title")
        blog.content = request.POST.get("content")
        blog.save()
    return HttpResponseRedirect("/")

def edit(request, id):
    try:
        blog = Blog.objects.get(id=id)

        if request.method =="POST":
            blog.title = request.POST.get("title")
            blog.content = request.POST.get("content")
            blog.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"blog": blog})
    except Blog.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def delete(request, id):
    try:
        blog = Blog.objects.get(id=id)
        blog.delete()
        return HttpResponseRedirect("/")
    except Blog.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
    

