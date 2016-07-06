from django.db import models
from django.utils import timezone


class Recipe(models.Model):
	Recipe_Title = models.CharField(max_length=50)
	Recipe_Tags = models.CharField(max_length=200)
	Recipe_Owner = models.ForeignKey('auth.User')
	Recipe_Ingredients = models.TextField()
	Recipe_Description = models.TextField()
	Recipe_Date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.Recipe_Title