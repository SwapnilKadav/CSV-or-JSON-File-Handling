from django.db import models

class Data(models.Model):
    employee_name = models.CharField(max_length=20)
    dob = models.DateField()
    state = models.CharField(max_length=20) 
    pincode = models.CharField(max_length=6)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    joining_month = models.CharField(max_length=10)
    joining_year = models.CharField(max_length=4)

    def __str__(self):
        return self.employee_name+self.dob+self.state+self.pincode+self.salary+self.joining_month+self.joining_year