from django.db.models import Avg, Max, Min
from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Products
from django.http import Http404
# Create your views here.

all_post=[
    {
        'slug':'Python-Programming',
        'title':'Python.py',
        'author':'Elii',
        'image':'python.svg',
        'date':date(1402,9,4),
        'short_desc':'this is about python',
        'content':'lorem*2',
    },
    {
        'slug':'C-Programming',
        'title':'C#',
        'author':'Elii',
        'image':'csharp.svg',
        'date':date(1402,9,3),
        'short_desc':'this is about c#',
        'content':'lorem*2',
    },
    {
        'slug':'PHP-Programming',
        'title':'PHP',
        'author':'Elii',
        'image':'php.svg',
        'date':date(1402,9,2),
        'short_desc':'this is about php',
        'content':'lorem*2',
    },
]

def get_date(post):
    return post['date']

def index(request):
    # d=list(all_post)
    # context={'a':d}
    # return render(request,'blogs/index.html',context)
    post_sorted=sorted(all_post,key=get_date)
    latest=post_sorted[-2:]
    #OR context={'latest_posts':latests} and put context in the place of the last one
    return render(request,'blogs/index.html',{'latest_posts':latest})

def all_posts(request):
    return render(request,'blogs/all_posts.html',{'all_posts':all_post})

def single_post(request,slug):
    post=next(post for post in all_post if post['slug']==slug)
    return render(request,'blogs/post.html',{'post':post})

def product_list(request):
    all_products=Products.objects.all().order_by('-price')
    numbers=all_products.count()
    info=all_products.aggregate(Avg('price'),Max('price'),Min('price'))
    return render(request,'blogs/product_list.html',{'all_products':all_products,'numbers':numbers,'info':info})

def product_detail(request,slug):
    # try:
    #     pro = Products.objects.get(id=product_id)
    # except:
    #     raise Http404
     pro = get_object_or_404(Products,slug=slug)
     return render(request,'blogs/product_details.html',{'pro':pro})