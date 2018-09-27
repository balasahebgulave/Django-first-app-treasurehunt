from django.db import models
from django.contrib.auth.models import User



class TreasureGram(models.Model):
	user=models.ForeignKey(User,on_delete=True)
	name=models.CharField(max_length=100)
	value=models.DecimalField(decimal_places=2,max_digits=5)
	material=models.CharField(max_length=100)
	location=models.CharField(max_length=100)
	image=models.ImageField(upload_to='', blank=True)

	def __str__(self):
		return self.name

# Create your models here.


