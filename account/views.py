from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth.decorators import login_required


'''
def home(request):
    return HttpResponse('This is the home page.')
def tenant(request):
    return HttpResponse('This is the page for the tenants.')
def landlord(request):
    return HttpResponse('This is the page for the landlords.')
'''
# Create your views here.

def home(request):
    return render(request, 'account/dashboard.html')

def tenant(request):
    tenants=Tenant.objects.all()
    return render(request, 'account/tenant.html',{'tenants': tenants})

def landlord(request):
    landlords= Landlord.objects.all()
    return render(request,'account/landlord.html', {'landlords': landlords})
@csrf_exempt
def registerPage(request):
	form= CreateUserForm()
	if request.method=='POST':
		form= CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	context={'form':form}
	return render(request,'account/register.html',context)
@csrf_exempt
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request,user)
				return redirect('home')
			else:
				messages.info(request, 'Username Or password is incorrect')
		context={}
		return render(request, 'account/login.html',context)
    
def logoutUser(request):
	logout(request)
	return redirect('login')