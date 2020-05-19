from django.test import TestCase
from .models import meeting, meetingminutes, resource, event

# Tests the 'meeting' model
class MeetingTitleTest(TestCase):
    def test_string(self):
        meet=meeting(meetingtitle="Meeting 1")
        self.assertEqual(str(meet), meet.meetingtitle)
    
    def test_table(self):
        self.assertEqual(str(meeting._meta.db_table), 'title')

# Tests the 'meetingminutes' model
class MeetingMinutesTest(TestCase):
    def test_string(self):
        meet=meetingminutes(minutestext="Minutes Text")
        self.assertEqual(str(meet), meet.minutestext)
    
    def test_table(self):
        self.assertEqual(str(meetingminutes._meta.db_table), 'meetingminutes')

# Tests the 'resource' model
class ResourceTest(TestCase):
    def test_string(self):
        res=resource(resourcename="Resource 1")
        self.assertEqual(str(res), res.resourcename)
    
    def test_table(self):
        self.assertEqual(str(resource._meta.db_table), 'resource')


# Tests the 'event' model
class EventTest(TestCase):
    def test_string(self):
        even=event(eventtitle="Event 1")
        self.assertEqual(str(even), even.eventtitle)
    
    def test_table(self):
        self.assertEqual(str(event._meta.db_table), 'event')