from django.conf import settings
from django.core.mail import send_mail
from .forms import NLSignUpForm
from django.shortcuts import render
from django.template import loader
# Create your views here.

def home(request):
	formHead = "Sign up for our newsletter!"
	form = NLSignUpForm(request.POST or None)

	context = {
		'form_head': formHead,
		'form': form,
	}
	if form.is_valid():
		instance = form.save(commit=False)
		instance = form.save()
		subject = "New Sign Up"
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]
		contact_message = "%s %s" % (instance.first_name, instance.email)
		send_mail(
			subject,
			contact_message,
			from_email,
			to_email,
			fail_silently=True,
		)
		send_to_signee(instance)
		context = {
			'form_head': "Thanks for signing up!",
			'form': "",
		}

	return render(request, 'newsletter/home.html', context)


def send_to_signee(instance):
	subject = "Thanks for Joining"
	from_email = settings.EMAIL_HOST_USER
	to_email = [instance.email]
	contact_message = """
	Hey {0}!

		We greatly appreciate your interest in learing more about Livinade!

	Thanks,

	The Livinade Team
	""".format(instance.first_name)
	ctx = {"first_name": instance.first_name,}
	html_message = loader.get_template('emailmarketing/SignUpThankYou.html').render(ctx)
	send_mail(
		subject,
		contact_message,
		from_email,
		to_email,
		fail_silently=True,
		html_message = html_message,
	)