from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Complaints, Profile
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
def front(request):
    return render (request,"front.html")
def login(request):
    if request.method =='POST':
        #import ipdb; ipdb.set_trace()
        rollNo = request.POST['rollNo']
        #rollNo = request.POST['rollNo'] 
        password = request.POST['password']

        #import ipdb; ipdb.set_trace()
        user = auth.authenticate(username=rollNo,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("complaints")
        else:
            messages.info(request,'invalid')
            return redirect("login")

    else: 
        return render(request,"login.html")
def signUp(request):
    context = {}
    if request.method =='POST':
        print('inside post')
        first_name = request.POST['first_name']
       # middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        phoneNo = request.POST['phoneNo']
        email = request.POST['email']
        rollNo = request.POST['rollNo']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        bday = request.POST['bday']
        #gender = request.POST['gender']
        #gender = request.POST['gender']
        #gender = request.POST['gender']
        # room

        #check pass 

        if password1==password2:
            if User.objects.filter(username=rollNo).exists():
                messages.info(request,'username taken')
                return redirect('signUp')
            elif User.objects.filter(email=email).exists(): 
                messages.info(request,'email taken') 
                return redirect('signUp')
            else:      
                print('trying to create user')
                user = User.objects.create_user(
                    username=rollNo,
                    password=password1,
                    email=email,
                    first_name=first_name,
                    #middle_name=middle_name,
                    last_name=last_name
                )
            user.save()
            Profile.objects.create(user=user, type='STUDENT',dob=bday)
            print('user created')
            return redirect('login')
        else:
            context['error'] = 'Password are not equal'
    return render(request,"signUp.html",context)
def list(request):
    if request.method == 'GET':
        complaints = Complaints.objects.all()
        return render(request, 'list.html', {'complaints': complaints})
    if request.method =='GET2':
        print('data save')
        desc = request.GET['desc']
        image = request.GET['image']
        user = request.user
       # Complaints.objects.create(user=user,type= )

        complaint_type = request.POST['customer-type']
        Correction: 'customer-type' > 'complaint-type'
        Complaint.objects.create(user=user, type=complaint_type)
       
        complaints = Complaints.objects.filter(
            desc = desc,
            image = image,
            user = user,

        )
        return render(request,'list.html')#,{'complaints': complaints})
def Electricity(request):
    if request.method =='POST':
        desc = request.POST['desc']
        image = request.POST['image']
        user = request.user
        complaint_type = request.POST['customer-type']
        Correction: 'customer-type' > 'complaint-type'
        Complaint.objects.create(user=user, type=Electricity)
        complaints = Complaints.objects.filter(
            desc = desc,
            image = image,
            user = user,

        )
        return render (request,"Electricity.html")
def Plumber(request):
    if request.method =='POST':
        desc = request.POST['desc']
        image = request.POST['image']
        user = request.user
        complaint_type = request.POST['customer-type']
        Correction: 'customer-type' > 'complaint-type'
        Complaint.objects.create(user=user, type=Plumber)
        complaints = Complaints.objects.filter(
            desc = desc,
            image = image,
            user = user,

        )
        return render (request,"Plumber.html")
def Air_conditioner(request):
    if request.method =='POST':
        desc = request.POST['desc']
        image = request.POST['image']
        user = request.user
        complaint_type = request.POST['customer-type']
        Correction: 'customer-type' > 'complaint-type'
        Complaint.objects.create(user=user, type=Air_conditioner)
        complaints = Complaints.objects.filter(
            desc = desc,
            image = image,
            user = user,

        )
        return render (request,"Air_conditioner.html")
def Room_cleaning(request):
    if request.method =='POST':
        desc = request.POST['desc']
        image = request.POST['image']
        user = request.user
        complaint_type = request.POST['customer-type']
        Correction: 'customer-type' > 'complaint-type'
        Complaint.objects.create(user=user, type=Room_cleaning)
        complaints = Complaints.objects.filter(
            desc = desc,
            image = image,
            user = user,

        )
        return render (request,"Room_cleaning.html")
def Carpanter(request):
    if request.method =='POST':
        desc = request.POST['desc']
        image = request.POST['image']
        user = request.user
        complaint_type = request.POST['customer-type']
        Correction: 'customer-type' > 'complaint-type'
        Complaint.objects.create(user=user, type=Carpanter)
        complaints = Complaints.objects.filter(
            desc = desc,
            image = image,
            user = user,

        )
        return render (request,"Carpanter.html")

def logout(request):
    auth.logout(request)
    return redirect('/')





