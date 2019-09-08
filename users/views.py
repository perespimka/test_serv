from django.shortcuts import render
from django.contrib.auth import logout, login
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm 
from blogs.models import BlogPost
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from blogs.views import trueuser

# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return HttpResponseRedirect(reverse('index'))
    context = {'form' : form}
    return render(request, 'registration/register.html', context)

@login_required
def userpage(request, user_username):
    user = User.objects.get(username=user_username)
    
    posts = BlogPost.objects.filter(owner=user).order_by('-date_added')
    context = {'posts' : posts, 'datuser' : user}
    return render(request, 'registration/userpage.html', context)
