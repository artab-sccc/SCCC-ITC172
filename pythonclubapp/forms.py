from django import forms
from .models import meeting, meetingminutes, resource, event

class ResourceForm(forms.ModelForm):
    class Meta:
        model=resource
        fields='__all__'

class MeetingForm(forms.ModelForm):
    class Meta:
        model=meeting
        fields='__all__'
        