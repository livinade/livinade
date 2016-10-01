from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	url(r'^u/(?P<username>[\w-]+)/$', views.user_profiles, name='profile'),
	# url(r'^login/$', user_login, name='login')
	url(r'^account/register/$', views.register, name='register'),
	url(r'^account/edit/$', views.edit, name='edit'),
	
	url(r'^account/login/$', auth_views.login, name='login'),
	url(r'^account/logout/$', auth_views.logout, name='logout'),
	url(r'^account/logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),

	url(r'^account/password-change/$', auth_views.password_change, name='password_change'),
	url(r'^account/password-change/done/$', auth_views.password_change_done, 
		name='password_change_done'),

	# restore password urls
	url(r'^account/password-reset/$', auth_views.password_reset, name='password_reset'),
	url(r'^account/password-reset/done/$', auth_views.password_reset_done, 
		name='password_reset_done'),
	url(r'^account/password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', 
		auth_views.password_reset_confirm, name='password_reset_confirm'),
	url(r'^account/password-reset/complete/$', auth_views.password_reset_complete, 
		name='password_reset_complete'),

]