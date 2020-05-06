from django.shortcuts import render
from .models import meeting, meetingminutes, resource, event

# Create your views here.
def index(request): 
    return render(request, 'pythonclubapp/index.html')

def getresources(request):
    type_list=resource.objects.all()
    return render(request, 'pythonclubapp/resources.html', {'type_list' : type_list})


