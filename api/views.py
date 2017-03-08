from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.generics import CreateAPIView, GenericAPIView
from django.views.generic import FormView, RedirectView
from rest_framework.generics import(
	ListCreateAPIView
)
from django.utils.translation import ugettext_lazy as _
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

@api_view(['GET'])
def folders(request):
	if request.method == 'GET':
		fold 	   = folder.objects.all().order_by('NameInEnglish')
		serializer = FolderSerializer(fold, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def folder_element(request,pk):
		track 	   = tracks.objects.filter(FolderAssociated=pk).order_by('TrackNameInEnglish')
		serializer = TracksSerializer(track,many=True)
		return Response(serializer.data)

    
@api_view(['GET'])
def about_us(request):
		matter     = aboutUs.objects.all()
		serializer = aboutUsSerializer(matter,many=True)
		return Response(serializer.data)

@api_view(['GET'])
def privacy_policy(request):
		matter     = privacyPolicy.objects.all()
		serializer = privacyPolicySerializer(matter,many=True)
		return Response(serializer.data)



class contactUsCreateApiView(generics.CreateAPIView):
    model 			= contactUs
    queryset 		= contactUs.objects.all()
    serializer_class = contactUsSerializer
    
    def post(self, request, format=None):
		serializer = contactUsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			content = { 'data' 	: serializer.data,
						'status': _('true')
						}
			return Response(content, status=status.HTTP_201_CREATED)
		contentt = { 'data' : serializer.data,
					'status': _('false')
					}	
		return Response(contentt, status=status.HTTP_400_BAD_REQUEST)



class tracksPostApiView(GenericAPIView):

	serializer_class = TracksPostSerializer
	queryset 		 = tracks.objects.all()

	
	def post(self,request,*args,**kwargs):
		print  self.request.data['id']
		# print "::::::::".idd
		queryset = tracks.objects.filter(FolderAssociated=self.request.data['id'])
		content = []
		for con in queryset:
			trackpath = str(con.TrackPath)
			trackpath = "{0}/media/{1}".format("http://127.0.0.1:8000",trackpath)
			mydict = {
			'TrackNameInEnglish':con.TrackNameInEnglish,
			'TrackNameInSpanish':unicode(con.TrackNameInSpanish),
			'TrackPath':trackpath,
			'trackFrombucket':con.trackFrombucket
			}
			print mydict
			content.append(mydict)
		return Response(content,status=status.HTTP_400_BAD_REQUEST)



contactUs = contactUsCreateApiView.as_view()  
folder_element_post = tracksPostApiView.as_view()
