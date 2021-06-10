from django.db import models

# Create your models here.

class Career(models.Model):
    Name =  models.CharField(max_length=122)
    Phone_Number = models.CharField(max_length=10)
    Email_address = models.EmailField(max_length=122)
    Message = models.TextField()
    College_name = models.CharField(max_length=122)
    Branch = models.CharField(max_length=122)
    Enrollment_no = models.CharField(max_length=12)
    

