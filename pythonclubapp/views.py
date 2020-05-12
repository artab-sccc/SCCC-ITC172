from django.shortcuts import render, get_object_or_404
from .models import meeting, meetingminutes, resource, event

# Create your views here.
def index(request): 
    return render(request, 'pythonclubapp/index.html')

def getresources(request):
    type_list=resource.objects.all()
    return render(request, 'pythonclubapp/resources.html', {'type_list' : type_list})

def getmeetings(request):
    type_list=meeting.objects.all()
    return render(request, 'pythonclubapp/meetings.html', {'type_list' : type_list})

def meetingdetails(request, id):
    meet=get_object_or_404(meeting, pk=id)
    location=meet.meetinglocation
    context={
        'meet' : meet,
        'location' : location,
    }
    return render(request, 'pythonclubapp/meetingdetails.html', context=context)