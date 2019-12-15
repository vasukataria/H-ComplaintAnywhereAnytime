from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.views import View

from .models import Complaints, Profile
from django.contrib import auth
from django.contrib.auth.models import User


def front(request):
    return render (request,"front.html")


def signUp(request):
    context = {}
    if request.method =='POST':
        print('inside post')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        #phoneNo = request.POST['phoneNo']
        email = request.POST['email']
        rollNo = request.POST['rollNo']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        bday = request.POST['bday']
        #gender = request.POST['gender']
        #gender = request.POST['gender']
        Gender = request.POST['Gender']
        Hostel = request.POST['Hostel']
        Floor  = request.Post['Floor']
        Room_number = request.Post['Room_number']
        phone_number = request.POST['phone_number']

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
                    last_name=last_name,
                    Gender = Gender,
                    Hostel = Hostel,
                    Floor = Floor,
                    Room_number = Room_number,
                    

                )
            user.save()
            Profile.objects.create(user=user, type='STUDENT',dob=bday)
            Profile.objects.create(user=user, type='STUDENT',Hostel=Hostel)
            Profile.objects.create(user=user, type='STUDENT',Floor=Floor)
            Profile.objects.create(user=user, type='STUDENT',Room_number=Room_number)
            Profile.objects.create(user=user, type='STUDENT',Gender=Gender)
            Profile.objects.create(user=user, type='STUDENT',Gender=phone_number)
            print('user created')
            return redirect('login')
        else:
            context['error'] = 'Password are not equal'
    return render(request,"signUp.html",context)


@login_required()
def list(request):
    if request.method == 'GET':
        complaints = Complaints.objects.all()
        return render(request, 'list.html', {'complaints': complaints})
    if request.method =='GET2':
        print('data save')
        desc = request.GET['desc']
        image = request.GET['image']
        user = request.user
        complaint_type = request.POST['customer-type']
        complaints = Complaints.objects.filter(
            desc = desc,
            image = image,
            user = user,

        )
        return render(request,'list.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

class NewComplaint(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'complaint_types': Complaints.COMPLAINTS_TYPES
        }
        return render(request, 'create_complaint.html', context=context)

class ComplaintListCreateView(LoginRequiredMixin, View):

    def get(self, request):
        print("Get all complaints from database")

        # Get all complaints. Recent complaints should be visible first
        complaints = Complaints.objects.all().order_by('-created_at')
        count = Complaints.objects.count()
        context = {
            'complaints': complaints,
            'count':count
        }

        return render(request, 'list.html', context)

    def post(self, request):
        print("Trying to create a new complaint")
        complaint_data = request.POST

        # TODO: We must validate the data we received in the request body(request.POST).
        # Image uploading in Django:
        # https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html

        new_complaint = Complaints.objects.create(
            type=complaint_data.get('complaint_type'),
            desc=complaint_data.get('complaint_desc'),
            # Uploaded files are available via request.FILES
            image=request.FILES.get('complaint-image'),
            # Logged in user is available via request.user
            user=request.user
        )

        print("Complaint successfully created. id: {}".format(new_complaint.id))
        return redirect("/complaints/{}".format(new_complaint.id))
        # return redirect(reverse('complaint-detail'), kwargs={'pk': new_complaint.id})


class ComplaintsDetailView(LoginRequiredMixin, View):
    def get(self, request, pk=None):
        print("Querying a single complaint with id {} from database".format(pk))
        # Query complaint from database. Raise 404 if complaint is not found.
        complaint = get_object_or_404(Complaints, pk=pk)
        return render(request, 'complaint_detail.html', context={'complaint': complaint})


class MyComplaints(LoginRequiredMixin, View):
    def get(self, request):
        complaints = Complaints.objects.filter(user=request.user).order_by('-created_at')
        count = Complaints.objects.count()
        context = {
            'complaints': complaints,
            'count':count
        }

        return render(request, 'list.html', context)
        return render(request, 'list.html', context)


class WorkerHome(LoginRequiredMixin, View):
    def get(self, request):
        complaints = Complaints.objects.filter(type=request.user).order_by('-created_at')
        count = Complaints.objects.count()
        context = {
            'complaints': complaints,
            'count':count
        }
class Home(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.profile.type == 'STUDENT':
            # Get complaints submitted by user
            complaints = Complaints.objects.filter(user=request.user).order_by('-created_at')
        else:
            # Get compalints registered against the user (Electrician, Carpenter etc.)
            complaints = Complaints.objects.filter(type=request.user.profile.can_workon()).order_by('-created_at')

        context = {
            'complaints': complaints,
            'count': complaints.count(),
            'user_type': request.user.profile.type
        }

        return render(request, 'home.html', context)



def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request,)
    else:
        form = FeedbackForm()
    return render(request,)