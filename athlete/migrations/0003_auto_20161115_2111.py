# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('athlete', '0002_athlete_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('skill_complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SubLevels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_level_name', models.CharField(max_length=20)),
                ('number_of_skills', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TrainingLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.CharField(max_length=10)),
                ('number_of_sublevels', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='sublevels',
            name='training_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athlete.TrainingLevel'),
        ),
        migrations.AddField(
            model_name='skills',
            name='sub_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athlete.SubLevels'),
        ),
    ]
