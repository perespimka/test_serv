from django.shortcuts import render
from .models import BlogPost, Commentary
from .forms import BPForm, CommentForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .parser_gz import ikz_func

def trueuser(request, user):
    if request.user != user:
        raise Http404

# Create your views here.
def index(request):
    posts = BlogPost.objects.order_by('-date_added') #!Внимание -date_added
    
    context = {'posts' : posts}
    return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
    if request.method != 'POST':
        form = BPForm()
    else:
        poster = BlogPost(owner=request.user)
        form = BPForm(data=request.POST, instance=poster)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    context = {'form' : form}
    return render(request, 'blogs/new_post.html', context)

@login_required    
def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    trueuser(request, post.owner)
    if request.method != 'POST':
        form = BPForm(instance=post)
    else:
        
        form = BPForm(data=request.POST, files=request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    context = {'post' : post, 'form' : form}
    return render(request, 'blogs/edit_post.html', context)

@login_required
def viewpost(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    usercheck = request.user == post.owner
    comments = Commentary.objects.filter(post=post).order_by('date_added')
    
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            coment = form.save(commit=False)
            coment.owner = request.user
            coment.post = post
            coment.save()
        return HttpResponseRedirect(reverse('viewpost', args=[post_id]))

    context = {'post' : post, 'usercheck' : usercheck, 'comments' : comments, 'form' : form}
    return render(request, 'blogs/viewpost.html', context)

def ikz_data(request):
    if request.method != 'POST':
        check = False
        data_ikz =()
    else:
        ikz = request.POST['ikz']
        data_ikz = ikz_func(ikz)
        check = True


    context = {'check' : check, 'data_ikz' : data_ikz}
    return render(request, 'blogs/ikz_data.html', context)