from django.conf.urls import url

from . import views

urlpatterns = [
	
	url(r'folder/$'							,views.folders),
	url(r'^folder/(?P<pk>[0-9a-z-]+)/$'		,views.folder_element),
	url(r'^get-tracks/'						,views.folder_element_post),
	url(r'^about-us/$'						,views.about_us),
	url(r'^privacy-policy/$'				,views.privacy_policy),
	url(r'^contact-us/$'					,views.contactUs),

    ]