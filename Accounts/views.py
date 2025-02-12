from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import update_session_auth_hash

# mail verify 
import uuid
from .models import *
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings

# Create your views here.
# Login 
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            prof = Profile.objects.get(user=user)
            if prof.is_verified is True:
                auth.login(request, user)
                messages.success(request, "User Logged in.")
                return redirect('home')
            else:
                messages.warning(request, "Please Check Your Email Verify your account...!")
            return redirect('login')
        else:
            messages.warning(request, "Wrong input")
            return redirect('login')
    return render(request, 'Accounts/login.html')
# Register 
def register(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        userName = request.POST['userName']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if len(password) == 0 and len(password1) == 0:
            messages.warning(request, "Input Password !!!")
        elif len(password) < 8:
            messages.warning(request, "Password at least 8 character")
        else:
            if password == password1:
                if User.objects.filter(username=userName).exists():
                    messages.warning(request, "Username Already Taken !!!")
                elif User.objects.filter(email=email).exists():
                    messages.warning(request, "email Already Taken !!!")
                else:
                    user = User.objects.create_user(first_name=firstName, last_name=lastName, username=userName,
                                                        email=email, password=password)
                    user.set_password(password)
                    user.save()
                    auth_token = str(uuid.uuid4())

                    pro_obj = Profile.objects.create(user=user, auth_token=auth_token)
                    pro_obj.save()
                    send_mail_registration(email, auth_token)
                    messages.success(request, "User Created !!!")
                    return render(request, 'accounts/success.html')
            else:
                messages.warning(request, "Password not matched !!!")

    return render(request, 'accounts/register.html')
def logout(request):
    auth.logout(request)
    messages.warning(request, "logout successful")
    return redirect('login')
def forgotten(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('newpassword')
        password1 = request.POST.get('newpassword1')
        if len(password) == 0 and len(password1) == 0:
            messages.warning(request, "Input Password !!!")
        elif len(password) < 8:
            messages.warning(request, "Password at least 8 character")
        else:
            if password == password1:
                if email:
                    user = User.objects.get(email=email)
                    user.set_password(password)
                    user.save()
                    update_session_auth_hash(request, user)
                    messages.success(request, "Password changed success")
                    return redirect('login')
                else:
                    messages.error(request, 'email not matched.')
            else:
                messages.error(request, 'Password not matched.')
            
    return render(request, 'Accounts/forgotten.html')

def success(request):
    return render(request,'Accounts/Success.html')

def fail(request):
    return render (request,"Accounts/Fail.html")

def send_mail_registration(email, token):
    subject = "Account Verification link"
    message = f'hi click the link for verify http://127.0.0.1:8000/Accounts/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    
def verify(request, auth_token):
    profile_obj = Profile.objects.filter(auth_token=auth_token).first()
    profile_obj.is_verified = True
    profile_obj.save()
    messages.success(request, 'your mail is verified')
    return redirect('login')