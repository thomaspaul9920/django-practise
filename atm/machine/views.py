# import email
from http.client import HTTPResponse
from pickle import GET
from re import template
import re
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User,transactions
from django.urls import reverse


def index(request):
    context = {}
    if request.method =="GET":
        return render(request,'machine/index.html',context)
    try:
        user = User.objects.get(email_id = request.POST["email_id"], password = request.POST["password"])
        context = {"user": user}
        return HttpResponseRedirect(reverse('machine:main', args=(user.id,)))
    except User.DoesNotExist:
        context = {"error":True, "email_id":request.POST["email_id"]}
        return render(request,'machine/index.html', context)
    


def signup(request):
    context = {}
    if request.method == 'GET':
        return render(request,'machine/signup.html',context)     
    try:
        email = User.objects.get(email_id = request.POST["email_id"])
        context = {"error":True,"first_name":request.POST['first_name'], "last_name":request.POST['last_name'], "email_id":request.POST['email_id'], "password":request.POST['password']}
        return render(request,'machine/signup.html', context=context)


    except User.DoesNotExist:
        user_obj = User()
        user_obj.first_name = request.POST['first_name']
        user_obj.last_name = request.POST['last_name']
        user_obj.email_id = request.POST['email_id']
        user_obj.password = request.POST['password']
        user_obj.save()
        try:
            transactions_obj = transactions.objects.get(user=user_obj.id)
        except:
            transaction_obj = transactions()
            transaction_obj.user = user_obj
            transaction_obj.save()

    return render(request,'machine/index.html')

def main(request, user_id):
    bal = transactions.objects.get(id=user_id)
    bal = random.balance
    context ={"balance":bal, "user":user_id}
    return render(request,'machine/main.html',context)
        
    
def deposit(request):
    pass
def withdraw(request):
    pass
