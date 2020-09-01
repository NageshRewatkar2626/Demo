from django.db import models


class Hospital(models.Model):
	Hospital_id=models.AutoField(primary_key=True)
	Hospital_name=models.CharField(max_length=50,unique=True)
	Bed_count=models.IntegerField()

class Doctor(models.Model):

	Doctor_id	=models.AutoField(primary_key=True)
	Doctor_name	=models.CharField(max_length=30)
	Joining_date=models.DateField(auto_now=False)
	Speciality	=models.CharField(max_length=30)
	Salary		=models.FloatField()
	Experiance	=models.IntegerField()
	hospital_id =models.ForeignKey(Hospital, on_delete=models.CASCADE)

