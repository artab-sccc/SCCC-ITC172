from django.test import TestCase
from .models import weightstat, Workout, Meals

class MealsTest(TestCase):
   def test_string(self):
       name=Meals(mealname="Cookies")
       self.assertEqual(str(name), name.mealname)

class WorkoutTest(TestCase):
   def test_string(self):
       name=Workout(workoutname="Push Ups")
       self.assertEqual(str(name), name.workoutname)


