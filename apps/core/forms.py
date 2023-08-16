from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class GamesForm(forms.ModelForm):
    tags_input = forms.CharField(label='Теги', required=False)
    
    class Meta:
        model = Games
        fields = ('name_item', 'heros', 'raritys', 'cells', 'quantity', 'price', 'image')
        widgets = {
            'name_item': forms.TextInput(attrs={'class': 'form-control'}),
            'heros': forms.Select(attrs={'class': 'form-control'}),
            'raritys': forms.Select(attrs={'class': 'form-control'}),
            'cells': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }