from django.db import models

# Create your models here.
class Item(models.Model):
	item = models.CharField(max_length=200)
	item_info = models.CharField(max_length=200, blank=True)
	checked = models.BooleanField()
	def __str__(self):
		return self.item

class Suggestions(models.Model):
	item = models.CharField(max_length=200)
	def __str__(self):
		return self.item