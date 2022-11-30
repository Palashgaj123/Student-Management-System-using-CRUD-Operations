from django.db import models

# Create your models here.
class stud_data1(models.Model):
    RollNo=models.IntegerField()
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Department=models.CharField(max_length=80)
    MobileNo=models.IntegerField()

class stud_login(models.Model):
    Email=models.EmailField(max_length=100)
    Password=models.TextField(max_length=50)

