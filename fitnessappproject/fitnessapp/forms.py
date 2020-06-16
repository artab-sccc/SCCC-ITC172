from django import forms
from .models import weightstat, Workout, Meals

class WorkoutForm(forms.ModelForm):
    class Meta:
        model=Workout
        fields='__all__'

class WeightForm(forms.ModelForm):
    class Meta:
        model=weightstat
        fields='__all__'

class MealForm(forms.ModelForm):
    class Meta:
        model=Meals
        fields='__all__'