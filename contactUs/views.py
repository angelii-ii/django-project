from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import userRegisterForm,userLoginForm,changePasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def contact(request):
    return render(request,'contactUs/contact_page.html')

def user_register(request):
    if request.method=='POST':
        form_register=userRegisterForm(request.POST)
        if form_register.is_valid():
            data=form_register.cleaned_data
            User.objects.create_user(username=data['user_name'],
                                     email=data['email'],
                                     first_name=data['first_name'],
                                     last_name=data['last_name'],
                                     password=data['password1'])
            return redirect('home:home-func')
    else:
        form_register=userRegisterForm()
    context={'form_register':form_register}
    return render(request,'contactUs/user_register.html',context)

#-------------login
def user_login(request):
    if request.method=='POST':
        form_login= userLoginForm(request.POST)
        if form_login.is_valid():
            data= form_login.cleaned_data
            user= authenticate(request,username=data['user'],
                               password=data['password'])
            if user is not None:
                login(request,user)
                return redirect('home:home-func')
    else:
        form_login= userLoginForm()
    return render(request,'contactUs/login.html',{'form_login':form_login})

#-----------------logout

def user_logout(request):
    logout(request)
    return redirect('home:home-func')

#------------------changepass

@login_required()
def change_password(request):
    if request.method=='POST':
        user=request.user
        form= changePasswordForm(request.POST)
        if form.is_valid():
            data= form.cleaned_data
            old_password= data['old_password']
            new_password1= data['new_password1']
            new_password2= data['new_password2']
            if not user.check_password(old_password):
                return HttpResponse('incorrect password')
            elif new_password1!=new_password2:
                return HttpResponse("new password doesn't match")
            else:
                user.set_password(new_password1)
                login(request,user)
                user.save()
                return HttpResponse('password changed!')
    else:
        form= changePasswordForm()
    return render(request,'contactUs/changepassword.html',{'form':form})