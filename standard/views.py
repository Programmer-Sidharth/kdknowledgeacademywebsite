from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Student, Fee
import random
from django.contrib.auth.models import User, auth

# Create your views here.
def profile(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user = authenticate(email=email, password=password)
        
    

def index(request):
    return render(request, 'index.html')

def standard(request, standard):

    context = {"standard":standard, 'title':f"class {standard}th cource"}
    return render(request, 'standardbatch.html', context)

def student(request, id):
    obj = Student.objects.get(id=id)
    name = obj.name
    rollno = id
    standard = obj.standard
    phone = obj.phone
    address = obj.address
    
    context = {"title":name, 'sname':name, "rollno":rollno, 'standard':standard, 'address':address, 'phone':phone}
    return render(request, 'student.html', context)


def login(request):
    context = {'title':'login'}
    return render(request, 'login.html', context)

def register(request):
    context = {'title':'Register'}
    return render(request, 'register.html', context)

def cources(request):
    classes = Fee.objects.all()
    context = {'classes':classes, 'title':'Cources'}
    return render(request, 'cources.html', context)



def students_on_class(request, standard):
    students = Student.objects.all()
    context = {'title':f'{standard}th students', 'students':students, 'standard':standard}
    return render(request, 'standard_students.html', context)

def registered(request):
    name = request.POST['name']
    standard = request.POST['standard']
    address = request.POST['address']
    phone = request.POST['phone']
    email = request.POST['email']
    password = request.POST['password']
    Student.objects.create(name=name, standard=standard, address=address, phone=phone, email=email, password=password)
    context = {'name':name, "standard":standard, "address":address, "phone":phone, 'title':'registered the user', "email":email}
    return render(request, 'userregistered.html', context)

def find_friends(request):
    context = {'title':'Find Friends'}
    return render(request, 'findfriends.html', context)


def friendifound(request):
    rollnum =request.POST['Rollno']
    try:
        if '@' not in rollnum:
            obj = Student.objects.get(id=rollnum)
        else:
            obj = Student.objects.get(email=rollnum)
        sname = obj.name
        standard = obj.standard
        rollno = obj.id
    except:
        return 404
    context = {"title":sname, 'sname':sname, "rollno":rollno, 'standard':standard}
    return render(request, 'student.html', context)