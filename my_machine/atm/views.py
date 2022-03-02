# import email
from crypt import methods
from http.client import HTTPResponse
from multiprocessing import context
from pickle import GET
from re import template
import re
from urllib import request
from urllib.parse import uses_relative
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User,transactions, history
from django.urls import reverse

def index(request):
    context = {}
    if request.method =="GET":
        # return HttpResponse("hello")
        return render(request,'atm/login.html',context)
    else:
        try:
            user = User.objects.get(email_id = request.POST["email_id"], password = request.POST["password"])
            user_id = user.id
        except User.DoesNotExist:
            return render(request,'atm/signup.html')
        return HttpResponseRedirect(reverse('atm:main', args=(user_id,)))
    


def signup(request):
    context = {}
    if request.method == 'GET':
        return render(request,'atm/signup.html',context)     
    try:
        email = User.objects.get(email_id = request.POST["email_id"])
        context = {"error":True,"first_name":request.POST['first_name'], "last_name":request.POST['last_name'], "email_id":request.POST['email_id'], "password":request.POST['password']}
        return render(request,'atm/signup.html/', context=context)


    except User.DoesNotExist:
        user_obj = User()
        user_obj.first_name = request.POST['first_name']
        user_obj.last_name = request.POST['last_name']
        user_obj.email_id = request.POST['email_id']
        user_obj.password = request.POST['password']
        user_obj.save()
        try:
            transaction_obj = transactions.objects.get(user=user_obj.id)
        except transactions.DoesNotExist:
            transaction_obj = transactions()
            transaction_obj.user = user_obj
            transaction_obj.save()
        
    # return render(request,'atm/login.html')
    return HttpResponseRedirect(reverse('atm:login'))

def main(request, user_id):
    transactions_obj = transactions.objects.get(id = user_id)
    deposit_url = f"http://127.0.0.1:8000/atm/{user_id}/main/deposit"
    withdraw_url = f"http://127.0.0.1:8000/atm/{user_id}/main/withdraw"
    statement_url = f"http://127.0.0.1:8000/atm/{user_id}/main/statement"
    context = {"transactions_obj":transactions_obj,"user_id":user_id,"deposit_url":deposit_url,"withdraw_url":withdraw_url, "statement_url":statement_url}
    # context = {"transactions_obj":transactions_obj,"user_id":user_id}
    return render(request,'atm/main.html', context)

        
    
def deposit(request, user_id):
    # return HttpResponse("Give Money pls i am poor thanks")
    if request.method == "POST":
        amount = request.POST["balance"]
        try:            
            user_obj = User.objects.get(id = user_id)
            transactions_obj = transactions.objects.get(id = user_id)
            transactions_obj.balance += float(amount)
            transactions_obj.save()
            entry = history()
            entry.user = user_obj
            entry.statements = f"Deposited {amount} rupees"
            entry.symbol = "+"
            entry.save()
            main_url = f"http://127.0.0.1:8000/atm/{user_id}/main"
            return HttpResponseRedirect(reverse('atm:main',args=(user_id,)))
        except Exception:
            context = {"error":True,"amount":amount}
            return render(request,'atm/deposit.html', context)
    else:
        return render(request, 'atm/deposit.html')
        
        
def withdraw(request, user_id):
    if request.method == "POST":
        print('------------------in POST')
        amount = request.POST["amount"]
        try:
            user_obj = User.objects.get(id=user_id)
            transaction_obj = transactions.objects.get(id=user_id)
            entry = history()
            entry.user = user_obj
            if transaction_obj.balance >= float(amount):
                transaction_obj.balance -= float(amount)
                transaction_obj.save()
            else:
                context = {"error":True}
                return render(request, 'atm/withdraw.html', context)
            entry.statements = f"Withdrew {amount} rupees"
            entry.symbol = "-"
            entry.save()
            main_url = f"http://127.0.0.1:8000/atm/{user_id}/main"
            return HttpResponseRedirect(reverse('atm:main',args=(user_id,)))
        except Exception:
            print('-------------------->>>>.qwer')
            context = {"error":True}
            return render(request, 'atm/withdraw.html', context)
    else:
        print('------------------------------>>>>')
        # return redirect('/atm/{}/main/withdraw/'.format(user_id))
        return render(request, 'atm/withdraw.html')

def statement(request, user_id):
    user_obj = User.objects.get(id=user_id)
    context = {"user":user_obj}
    return render(request, 'atm/statement.html',context)
