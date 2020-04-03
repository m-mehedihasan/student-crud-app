from django.db import models

class Student(models.Model):
	roll = models.IntegerField()
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	Class = models.CharField(max_length=30)
	email = models.EmailField(max_length=50)

	class Meta:
		db_table = 'Students'
