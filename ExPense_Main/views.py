from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#----------------------------------------------------------------

from .models import Income, Expense, UserProfile
from decimal import Decimal

# Create your views here.
def index(request):
    
    return render(request, 'index.html')


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if len(password1) < 8:
                messages.info(request, "Password must be at least 8 characters")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                balance = UserProfile.objects.create(balance=Decimal(-1.10), user=user)
                balance.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matching!')
            return redirect('register')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    balance = UserProfile.objects.get(user=request.user)
    
    if balance.setup == False:
        return redirect('setup')
    
    
    expenses = Expense.objects.all().filter(user=request.user.id).order_by('-id')[:1]
    incomes = Income.objects.all().filter(user=request.user.id).order_by('-id')[:1]
    monthlyIncome = Income.objects.all()
    monthlyExpense = Expense.objects.all()
    totalIncome = 0
    totalExpense = 0
    for m in monthlyIncome:
        totalIncome = totalIncome + m.amount
    for m in monthlyExpense:
        totalExpense = totalExpense + m.amount
    context = {"balance": balance,
               "expenses": expenses,
               "incomes": incomes,
               "monthlyIncome": totalIncome,
               "monthlyExpense": totalExpense}
    
    if request.method == 'POST':
        if request.POST['income'] == "1":
            newIncome = Income.objects.create(amount = request.POST['amount'], source = request.POST['source'], date = request.POST['date'], user = request.user)
            balance.balance = Decimal(newIncome.amount) + balance.balance
            balance.save()


        if request.POST['expense'] == "1":
            newExpense = Expense.objects.create(amount = request.POST['amount'], category = request.POST['category'], date = request.POST['date'], user = request.user)
            balance.balance = balance.balance - Decimal(newExpense.amount) 
            balance.save()

       
 

    return render(request, 'dashboard.html', context)

def setup(request):
    if request.method == 'POST':
        balance = UserProfile.objects.get(user=request.user)
        balance.balance = request.POST['balance']
        balance.setup = True
        balance.save()
    
        return redirect('dashboard')
    return render(request, 'setup.html')

def features(request):
    return render(request, 'features.html')

def income(request):
    return render(request, 'income.html')