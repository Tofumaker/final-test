from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from . import models

from .models import Entry, Comment

def index(request):
    latest_blog_list = Entry.objects.order_by('-created')[:5]
    context = {'latest_blog_list': latest_blog_list,}
    return render(request, 'blog/index.html', context)

def detail(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    comments = Comment.objects.filter(entry=entry_id)
    context = {'entry': entry, 'comments': comments}
    return render(request, 'blog/detail.html', context)

def new_comment(request, entry_id):
    print entry_id
    entry = get_object_or_404(Entry, pk=entry_id)
    author = request.POST['author']
    message = request.POST['message']
    comment = Comment.objects.create(author = author, body=message, entry=entry)
    url = "/blog/"+str(entry_id)
    return redirect(url)
