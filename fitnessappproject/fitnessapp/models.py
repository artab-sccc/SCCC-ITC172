from django.db import models
from django.contrib.auth.models import User

class weightstat(models.Model):
    weight=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    height=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    weightdate=models.DateField()

    def int(self):
        return self.weight
    
    class Meta:
        db_table='weightstat'
        verbose_name_plural='weightstats'

class Workout(models.Model):
    currentweight=models.ForeignKey(weightstat, on_delete=models.DO_NOTHING)
    workoutname=models.CharField(max_length=255)
    minutes=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    reps=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sets=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    workoutdate=models.DateField()

    def __str__(self):
        return self.workoutname
    
    class Meta:
        db_table='workout'
        verbose_name_plural='workouts'

class Meals(models.Model):
    currentweight=models.ForeignKey(weightstat, on_delete=models.DO_NOTHING)
    mealname=models.CharField(max_length=255)
    mealcalories=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    mealcarbs=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    mealprotien=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    mealfats=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    mealdate=models.DateField()

    def __str__(self):
        return self.mealname
    
    class Meta:
        db_table='meal'
        verbose_name_plural='meals'


