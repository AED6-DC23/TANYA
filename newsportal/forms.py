from django import forms
from .models import Post, Comment
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy

class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'author',
           'categoryType',
           'title',
           'text',
           'files',
       ]

   def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        title = cleaned_data.get("title")

        if title == text:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data

class CommForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'message',
            'text',

        ]
        labels = {
            'author': 'Автор',
            'message': 'Cooбщение',
            'text': 'Текст'
        }
