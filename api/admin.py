from django.contrib import admin
from .models import *
# Register your models here.



class TracksInline(admin.TabularInline):
	# list_display = ("TrackNameInEnglish","TrackNameInSpanish","TrackPath")
	exclude = ('trackFrombucket',)
	model = tracks
	extra = 3


class FolderModelAdmin(admin.ModelAdmin):
	inlines = ( TracksInline,)

	class Meta:
		model = folder


class TracksModelAdmin(admin.ModelAdmin):
	exclude = ('trackFrombucket',)
	model = tracks


admin.site.register(folder, FolderModelAdmin)
admin.site.register(tracks,TracksModelAdmin)
admin.site.register(aboutUs)
admin.site.register(privacyPolicy)
admin.site.register(contactUs)
