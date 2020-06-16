from django.shortcuts import render
from .models import weightstat, Workout, Meals
from. forms import WorkoutForm, WeightForm, MealForm
from django.contrib.auth.decorators import login_required

def index (request):
    return render(request, 'fitnessapp/index.html')

def getweight(request):
    type_list=weightstat.objects.all()
    return render(request, 'fitnessapp/weight.html', {'type_list' : type_list})

def getworkout(request):
    type_list=Workout.objects.all()
    return render(request, 'fitnessapp/workout.html', {'type_list' : type_list})

def getmeals(request):
    type_list=Meals.objects.all()
    return render(request, 'fitnessapp/meals.html', {'type_list' : type_list})

@login_required
def newWorkout(request):
     form=WorkoutForm
     if request.method=='POST':
          form=WorkoutForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=WorkoutForm()
     else:
          form=WorkoutForm()
     return render(request, 'fitnessapp/newworkout.html', {'form': form})

@login_required
def newWeight(request):
     form=WeightForm
     if request.method=='POST':
          form=WeightForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=WeightForm()
     else:
          form=WeightForm()
     return render(request, 'fitnessapp/newweight.html', {'form': form})

@login_required
def newMeal(request):
     form=MealForm
     if request.method=='POST':
          form=MealForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MealForm()
     else:
          form=MealForm()
     return render(request, 'fitnessapp/newmeal.html', {'form': form})

def loginmessage(request):
    return render(request, 'fitnessapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'fitnessapp/logoutmessage.html')

    