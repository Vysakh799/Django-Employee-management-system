from django.db import models

# Create your models here.
class employee(models.Model):
    emp_id=models.CharField(max_length=6)
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.CharField(max_length=20)
    phno=models.IntegerField()
    address=models.TextField()
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    status=models.CharField(max_length=20)
    def __str__(self):
        return self.name

