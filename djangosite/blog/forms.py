from django import forms
from  .models import *


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-control'}))
    slug = forms.SlugField(max_length=255, label='URL', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-control'}),
                              label='Статья')
    is_published = forms.BooleanField(label='Публикация', required=False, initial=True,
                                      widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),
                                 label='Категории',
                                 empty_label='Категория не выбрана',
                                 widget=forms.Select(attrs={'class': 'form-control'}))
