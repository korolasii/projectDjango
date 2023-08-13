from django import forms
from django.utils.text import slugify
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
        
class ArticleForm(forms.ModelForm):
    tags_input = forms.CharField(label='Теги', required=False)
    class Meta:
        model = Article
        fields = ('title', 'category', 'content_preview', 'content', 'status', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            'content_preview': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            tags = ', '.join([tag.name for tag in self.instance.tags.all()])
            self.initial['tags_input'] = tags
        
    def save(self, commit=True):
        article = super().save(commit=False)
               
        if commit:
            article.save()      
               
               
            tags = self.cleaned_data['tags_input']
            if tags:
                tags_list = [tag.strip() for tag in tags.split(', ')]
                
                # delete old tags
                if self.instance.pk:
                    self.instance.tags.clear()
                    
                for tag in tags_list:
                    if not tag:
                        continue
                    tag_obj, _ = Tag.objects.get_or_create(name=tag)
                    article.tags.add(tag_obj)
                
        
        return article