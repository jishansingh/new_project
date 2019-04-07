from django import forms
from .choices import *
class post(forms.Form):
	url=forms.CharField(max_length=100)
	name=forms.CharField(max_length=50)

class my_blog(forms.Form):
	data=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Whats on your mind??'}))

class new_blog(forms.Form):
	title=forms.CharField(max_length=30)

class new_pro(forms.Form):
	category = forms.ChoiceField(choices = CHOICE, label="", initial='', widget=forms.Select(), required=True)
	file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	title=forms.CharField(max_length=50)
	image=forms.FileField()
	description=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'tell us more about product'}))
	phone_number=forms.IntegerField()
	name=forms.CharField(max_length=50)