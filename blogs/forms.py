from django import forms
from .models import BlogPost, Commentary
from django.contrib.auth.forms import UserCreationForm

class BPForm(forms.ModelForm):
    class Meta():
        model = BlogPost
        fields = ['title', 'text', 'image']
        labels = {'title' : '', 'text' : '', 'image' : 'Загрузить изображение'}
        widgets = {'text' : forms.Textarea(attrs={'cols':80})}

class CommentForm(forms.ModelForm):
    class Meta():
        model = Commentary
        fields = ['text']
        labels = {'text' : ''}
        widgets = {'text' : forms.Textarea(attrs={'cols':40})}