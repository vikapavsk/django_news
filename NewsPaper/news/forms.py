from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'author',
           'categoryType',
           'category',
           'title',
           'text',
       ]

   def clean(self):
       cleaned_data = super().clean()
       title = cleaned_data.get("title")
       if title is not None and len(title) < 5:
           raise ValidationError({
               "title": "Название не может быть менее 5 символов."
           })

       return cleaned_data