from django import forms
from .models import NLSignUp
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import FormActions

class NLSignUpForm(forms.ModelForm):
	class Meta:
		model = NLSignUp
		fields = [
			"first_name",
			"email",
		]

	# validator overides
	def clean_email(self):
		email =  self.cleaned_data.get('email')
		#email_base, provider = email.split('@')
		#domain, extention = provider.split('.')
		#if not domain == "imawesome":
			#raise forms.ValidationError("Please use proper buttfuck email")
		#if not extention == 'edu':
			#raise forms.ValidationError("Please use a valid .edu address")
		return email

	def clean_first_name(self):
		first_name = self.cleaned_data.get('first_name')
		# write some validations
		return first_name

	@property
	def helper(self):
		helper = FormHelper()
		helper.form_id = 'id-exampleForm'
		helper.form_method = 'post'
		helper.form_action = '#thanks'
		helper.form_class = 'form-inline'
		helper.field_template = 'bootstrap3/layout/inline_field.html'
		helper.layout = Layout(
			'first_name',
			'email',
			FormActions(
                Submit('submit', 'Sign Up', css_class="btn btn-primary btn-block"),
            )
		)
		return helper