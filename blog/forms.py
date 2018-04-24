from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegisterForm(UserCreationForm):
	
	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		self.fields['username'].label = 'Имя пользователя'
		self.fields['password1'].label = 'Пароль'
		self.fields['password2'].label = 'Подтверждение пароля'


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)