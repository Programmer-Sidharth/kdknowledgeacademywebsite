from django.db import models

class Fee(models.Model):
    standard = models.IntegerField(unique=True)
    fee = models.IntegerField()
    def __str__(self):
        return f"class {self.standard} fee = {self.fee} Rs."

class Student(models.Model):
    name = models.CharField(max_length=45, null=False, unique=True)
    standard = models.IntegerField(null=True)
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
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


class Alert(models.Model):
    page_name = models.CharField(max_length=100)
    AlertTopic = models.CharField(max_length=100)
    AlertMessage = models.CharField(max_length=100)


