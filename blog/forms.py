from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms.formsets import BaseFormSet

from .models import Article, Tag


class RegisterForm(UserCreationForm):
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].label = 'Имя пользователя'
		self.fields['password1'].label = 'Пароль'
		self.fields['password2'].label = 'Подтверждение пароля'


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	


class ArticleForm(forms.ModelForm):
	
	class Meta:
		model = Article
		fields = ['title', 'text']
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['title'].label = 'Название статьи'
		self.fields['text'].label = 'Статья'
		

class TagForm(forms.ModelForm):
	
	class Meta:
		model = Tag
		fields = ['name']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].widget.attrs['required'] = 'required'
		

class BaseTagFormSet(BaseFormSet):
	
	def clean(self):
		if any(self.errors):
			return
			
		for form in self.forms:
			if form.cleaned_data:
				tag = form.cleaned_data['name']
				if tag:
					if Tag.objects.filter(name=tag).exists() != True:
						t = Tag.objects.create(name=tag)
						t.save()
					else:
						pass
						
		

		
