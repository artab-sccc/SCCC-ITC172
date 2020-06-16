from django.contrib import admin
from .models import weightstat, Workout, Meals

admin.site.register(weightstat)
admin.site.register(Workout)
admin.site.register(Meals)