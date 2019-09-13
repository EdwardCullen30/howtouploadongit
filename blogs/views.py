# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def blogs_show_all(request):
	blogger=Blogger.objects.filter(username=request.user.username)
    if blogger:
        blogger=blogger[0]
    blogs_list=Post.objects.order_by('-pub_date')[:]
    paginator=Paginator(blogs_list,5)
    page=request.GET.get('page',1)
    blogs=paginator.page(page)
    return render(request,'blogs/blogs_page.html',{'blog_list':blogs,'blogger':blogger})

def all_bloggers(request):
    bloggers_list=Blogger.objects.order_by('blogger_name')
    return render(request,'blogs/all_bloggers.html',{'bloggers_list':bloggers_list})    
	

# Create your views here.
