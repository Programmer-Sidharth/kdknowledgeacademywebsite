from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
import random
from django.contrib import auth as auth_view
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def profile(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth_view.authenticate(username=username, password=password)
        if user is not None:
           messages.info(request, "You're logged In Successfully!", extra_tags=f'Hi {user.username}')
        else:
            messages.info(request, 'Wrong Credentials!', extra_tags='Wrong Username or Password')
            return redirect('/login')
        auth_view.login(request, user)
        return redirect('/')
    else:
        return redirect('/login')
def index(request):
    context = {'title':"Home"}
    return render(request, 'index.html', context)

def standard_details(request, standard):
    context = {"standard":standard, 'title':f"class {standard}th cource", 'class':standard}
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
    classes = Fee.objects.all()
    context = {'title':'Register', 'classes':classes}
    return render(request, 'register.html', context)

def cources(request):
    messages.info(request, 'Get MORE at low Prices', extra_tags='CoronaVirus Sale')
    classes = Fee.objects.all()
    context = {'classes':classes, 'title':'Cources'}
    return render(request, 'cources.html', context)


def students_on_class(request, standard):
    students = Student.objects.all()
    context = {'title':f'{standard}th students', 'students':students, 'standard':standard}
    return render(request, 'standard_students.html', context)

def registered(request):
    username = request.POST['username']
    name = request.POST['name']
    standard = request.POST['standard']
    email = request.POST['email']
    password = request.POST['password']
    try:
        messages.info(request, 'Your account is created!', extra_tags=f'Hi {username}')
        User.objects.create_user(username=username, first_name=name, password=password, email=email)
        user = auth_view.authenticate(username=username, password=password)
        auth_view.login(request, user)
    except:
        messages.info(request, 'Login to your account', extra_tags='Account Already Exists!')
        return redirect('/login')
    context = {'name':name, "standard":standard, 'title':'registered the user', "email":email}
    return redirect('/')

def search_students(request):
    context = {'title':'search students'}
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



def friendRelated(request):
    Area = request.POST['Rollno']
    # if Area == '':
    #         return redirect('/')
    if request.method == 'post':
        try:
            results_id = Student.objects.filter(id=Area)
        except:
            pass
        try:
            results_name = User.objects.filter(standard__icontains=Area)
        except:
            pass
        try:
            results_email = User.objects.filter(email__icontains=Area)
        except:
            pass
        try:
            results_username = User.objects.filter(username__icontains=Area)
        except:
            pass
        params = {'id':results_id, 'name':results_name, 'email':results_email, 'title':'search results'}
        return render(request, 'search_results_of_students.html', params)
    else:
        return redirect('/')

def buy_cource(request, standard):
    if User.is_authenticated:
        context = {'class':standard, 'title':'Buy Cource'}
        return render(request, 'buycource.html', context)
    else:
        messages.info(request, 'You Need To Login To Your Account Or Create Account First', extra_tags='You are Anonymous User! ')
        return redirect('/login')

def logout(request):
    auth_view.logout(request)
    messages.info(request, 'Login to your another account', extra_tags='You are logged out successfully!')
    return redirect('/login')


def editingProfile_home(request):
    if User.is_authenticated:
        classes = Fee.objects.all()
        context = {'title':'Profile', 'classes':classes}
        return render(request, 'profile.html', context)
    else:
        return redirect('/login')


def updateProfile(request):
    name = request.POST['name']
    email = request.POST['email']
    standard = request.POST['standard']
    phone = request.POST['phone']
    obj, created = Student.objects.update_or_create(name=User.username,
    defaults={'email': email, 'standard':standard, 'phone':phone},
)
    if created:
        messages.info(request, 'Your details are Created!', extra_tags='Congratulations!')
    else:
        messages.info(request, 'Your details are updated!', extra_tags='Congratulations!')
    return redirect('/profile')
