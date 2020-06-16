# Generated by Django 3.0.5 on 2020-06-16 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeightStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'verbose_name_plural': 'weightstats',
                'db_table': 'weightstat',
            },
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workoutname', models.CharField(max_length=255)),
                ('minutes', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('reps', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sets', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('workoutdate', models.DateField()),
                ('currentweight', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fitnessapp.WeightStat')),
            ],
            options={
                'verbose_name_plural': 'workouts',
                'db_table': 'workout',
            },
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mealname', models.CharField(max_length=255)),
                ('mealcalories', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('mealcarbs', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('mealprotien', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('mealfats', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('mealdate', models.DateField()),
                ('currentweight', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fitnessapp.WeightStat')),
            ],
            options={
                'verbose_name_plural': 'meals',
                'db_table': 'meal',
            },
        ),
    ]
