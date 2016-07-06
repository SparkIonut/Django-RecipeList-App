# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 18:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Recipe_Title', models.CharField(max_length=50)),
                ('Recipe_Tags', models.CharField(max_length=200)),
                ('Recipe_Ingredients', models.TextField()),
                ('Recipe_Description', models.TextField()),
                ('Recipe_Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Recipe_Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]