from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from Treasure.models import TreasureGram
from Treasure.forms import TreasureForm
from Treasure.forms import TreasureCustom
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm


def home(request):
	all_treasure=TreasureGram.objects.all()
	return render (request,'Treasure/home.html',{'all_treasure':all_treasure})

def detail(request,val):
	treasure=TreasureGram.objects.get(id=val)
	return render (request,'Treasure/detail.html',{'val':treasure})

def add_new(request):
	form=TreasureForm()

	if request.method == 'POST':

		form=TreasureForm(request.POST, request.FILES)
		
		if form.is_valid():
			form=form.save()
			form.save()
			return redirect('/home/')
		else:
			
			form.errors
	else:
		form=TreasureForm()
	return render(request,'Treasure/new_treasure.html',{'form':form})


def customview(request):
	form=TreasureCustom()
	if request.method=='POST':
		form=TreasureCustom(request.POST,request.FILES)
		if form.is_valid():
			form.save()
		return redirect('/home/')
	else:
		form=TreasureCustom()
		return render(request,'Treasure/custom.html',{'form':form})



# Create your views here.


def edit(request,val):
	if request.method=='GET':
		treasure=TreasureGram.objects.get(id=val)
		form=TreasureForm(instance=treasure)
		return render(request,'Treasure/edit.html',{'form':form})
	else:
		treasure=TreasureGram.objects.get(id=val)
		form=TreasureForm(request.POST,request.FILES,instance=treasure)
		form.save()
		return redirect ('/home/')


def loginform(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data['username']
			raw_password=form.cleaned_data['password1']
			user=authenticate(username=username,password=raw_password)
			login(request,user)
			return redirect('/home/')
		else:
			return HttpResponse('Your password cant be too similar to your other personal information.')
	else:
		form=UserCreationForm()
		return render(request,'Treasure/login.html',{'form':form})

def logoutform(request):
	logout(request)
	return redirect('/home/')
