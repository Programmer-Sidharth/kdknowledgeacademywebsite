from django.db import models



class Fee(models.Model):
    standard = models.IntegerField(unique=True)
    fee = models.IntegerField()
    def __str__(self):
        return f"class {self.standard} fee = {self.fee} Rs."



# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=35, null=False)
    standard = models.IntegerField(null=False)
    phone = models.IntegerField(null=False)
    address = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20, null=True)
    def __str__(self):
        return f"{self.name} class={self.standard} rollno={self.id}"


class Course(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    publish_Date = models.TimeField(auto_now_add=True)
    standard = models.IntegerField(null=False)
    description = models.TextField(max_length=200)
    timings = models.CharField(max_length=20)
    venue = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}, class {self.standard} .... {self.price}Rs."