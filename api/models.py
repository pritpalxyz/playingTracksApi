from __future__ import unicode_literals
import uuid
from django.db import models
from django.core.validators import MinValueValidator
from timezone_field import TimeZoneField
from django.utils import timezone
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
import random
import os
import string
import uuid

def get_capture_upload_path(instance, filename):
	# capture_folder_name = "%s_%s" % ("Y" if instance.form_data else "N", instance.capture_id)
	filename  = "{0}_{1}".format(str(uuid.uuid4()),filename)
	folder_altername_name =  str(uuid.uuid4())
	folder_path = os.path.join(settings.MEDIA_SUB_FOLDER_NAME, 'tracks_all',folder_altername_name)
	folder_root = os.path.join(settings.MEDIA_ROOT, folder_path)

	if not os.path.exists(folder_root):
		os.makedirs(folder_root)

	return os.path.join(folder_path, filename)


class folder(models.Model):
	id					    = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	NameInEnglish			= models.CharField(max_length=200,verbose_name="Book in English")
	NameInSpanish			= models.CharField(max_length=200,verbose_name="Book in Spanish")

	def __unicode__(self):
		return self.NameInEnglish

	def __unicode__(self):
		return self.NameInSpanish

	class Meta:
		ordering = ('NameInEnglish',)
		verbose_name = 'Book'
		verbose_name_plural = "Books"


class tracks(models.Model):
	id					    = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	TrackNameInEnglish		= models.CharField(max_length=200,verbose_name="Chapter in English")
	TrackNameInSpanish		= models.CharField(max_length=200,verbose_name="Chapter in Spanish")
	FolderAssociated        = models.ForeignKey(folder,verbose_name='Select Book')
	TrackPath               = models.FileField(upload_to=get_capture_upload_path,verbose_name='Upload Chapter')
	trackFrombucket          =  models.CharField(max_length=2000,default='')
	def __unicode__(self):
		return self.TrackNameInEnglish

	def __unicode__(self):
		return self.TrackNameInSpanish

	class Meta:
		ordering = ('TrackNameInEnglish',)
		verbose_name = 'Chapter'
		verbose_name_plural = "Chapters"

class aboutUs(models.Model):
	contentInEnglish					= models.TextField(null=True, blank=True,verbose_name="About in English")
	contentInSpanish					= models.TextField(null=True, blank=True,verbose_name="About in Spanish")

	def __unicode__(self):
		return self.contentInEnglish

	def __unicode__(self):
		return self.contentInSpanish

	class Meta:
		verbose_name = 'About'
		verbose_name_plural = "About Us"

class privacyPolicy(models.Model):
	contentInEnglish					= models.TextField(null=True, blank=True,verbose_name="Privacy Policy in English")
	contentInSpanish					= models.TextField(null=True, blank=True,verbose_name="Privacy Policy in Spanish")

	def __unicode__(self):
		return self.contentInEnglish

	def __unicode__(self):
		return self.contentInSpanish


	class Meta:
		verbose_name = 'Privacy Policy'
		verbose_name_plural = "Privacy Policy"

class contactUs(models.Model):
	name		= models.CharField(max_length=200)
	email		= models.CharField(max_length=200)
	message     = models.CharField(max_length=200)

	def __unicode__(self):
		return self.email
