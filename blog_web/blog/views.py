from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'name' : 'suchir',
        'title' : 'Blog  1',
        'content' : 'first post',
        'date_posted' : 'March 22,2024'
    },
     {
        'name' : 'kumar',
        'title' : 'Blog  2',
        'content' : 'second post',
        'date_posted' : 'March 23,2024'
    }
]

def home(request):
    context = {
        'posts' : posts,
        'title' : 'Home'
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title' : 'About'})