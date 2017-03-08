from rest_framework import serializers
from .models import *


class FolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = folder
        fields = ('id', 'NameInEnglish', 'NameInSpanish',)


class TracksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = tracks
        fields = ['id', 'TrackNameInEnglish', 'TrackNameInSpanish','TrackPath','trackFrombucket']

class TracksPostSerializer(serializers.ModelSerializer):
    id =serializers.CharField()
    class Meta:
        model = tracks
        fields = ['id',]


class aboutUsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = aboutUs
        fields = ('contentInEnglish','contentInSpanish')

class privacyPolicySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = privacyPolicy
        fields = ('contentInEnglish','contentInSpanish')

class contactUsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = contactUs
        fields = ('name','email','message')

