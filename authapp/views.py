from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate,login,logout


# Create your views here.


def index(request):
    return render(request,'index.html')

def signup(request):
    usr  = usermodel.objects.all()
    form = RegistrationForm()
    if request.method=='POST':
        form = RegistrationForm(data = request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if len(password)<8:
                messages.success(request,message='password must be 8 character long')
            else:
                user = form.save(commit=False)
                user.set_password(user.password)
                user.save()
                usermodel.objects.create(user=user,phno=form.cleaned_data['phone_no'])

                form = RegistrationForm()
                return redirect('authapp:login')
    else:
        form =RegistrationForm()
    return render(request,'signup.html',{'form':form})



def userLogin(request):
    form = LoginForm()
    if request.method=='POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username=data['username'],password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('authapp:profile')
            else:
                messages.success(request, 'acc disabled')
    else:
        form = LoginForm()
    return render(request,'Login.html',{'form':form})






def profile(request):
    user = User.objects.get(id=request.user.id)
    usr = usermodel.objects.get(user=user)

    return render(request,'profile.html',{'details':user,'phno':usr})

def usr_logout(request):
    logout(request)
    return render(request,'index.html')