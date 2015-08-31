from django import forms
from .models import SignUp

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		print email_base
		print provider
		domain, extension = provider.split('.')
		print domain
		print extension

		#if not domain == 'uwm':
		#	raise forms.ValidationError("Please use your valid UWM email.")
		# if not extension == 'edu':
		# 	raise forms.ValidationError("Please use a valid .EDU email address")
		return email

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name','email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		print email_base
		print provider
		domain, extension = provider.split('.')
		print domain
		print extension

		#if not domain == 'uwm':
		#	raise forms.ValidationError("Please use your valid UWM email.")
		#if not extension == 'edu':
		#	raise forms.ValidationError("Please use a valid .EDU email address")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		#Write validation code here.
		return full_name