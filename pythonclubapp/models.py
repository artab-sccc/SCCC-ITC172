from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.DecimalField(max_digits=4, decimal_places=0)
    meetinglocation=models.CharField(max_length=255)
    meetingagenda=models.TextField()

    def __str__(self):
        return self.meetingtitle

    class Meta():
        db_table='title'
        verbose_name_plural='titles'

class meetingminutes(models.Model):
    meetingid=models.ForeignKey(meeting,on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutestext=models.TextField()

    def __str__(self):
        return self.minutestext
    
    class Meta():
        db_table='meetingminutes'
        verbose_name_plural='meetingminutes'
    

class resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceurl=models.URLField(null=True, blank=True)
    dateentered=models.DateField()
    userid=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    description=models.TextField()

    def __str__(self):
        return self.resourcename
    
    class Meta():
        db_table='resource'
        verbose_name_plural='resoruces'

class event(models.Model):
    eventtitle=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.DecimalField(max_digits=4, decimal_places=0)
    eventdescription=models.TextField()
    eventuserid=models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventtitle

    class Meta():
        db_table='event'
        verbose_name_plural='events'

