from django import forms
from app_blog.models import Blog,Comment

class CommetnForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ('comment',)
