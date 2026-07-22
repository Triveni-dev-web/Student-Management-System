from django.db import models
class Student(models.Model):
    name =models.CharField(max_length=100)
    rollno=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    branch=models.CharField(max_length=50)
    def __str__(self):
        return self.name                            

# Create your models here.
