from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from bankapp.models import newplace


def signin(request):
    if request.method =='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request, "application.html")
        else:
            messages.info(request,"invalid credentials")
            return redirect('signin')

    return render(request,"signin.html")


def signup(request):
    if request.method=='POST':
       email=request.POST['email']
       password = request.POST['password']
       confirm_password = request.POST['confirm_password']

       if password==confirm_password:
             if User.objects.filter(username=email).exists():
                messages.info(request,"User alredy Exist")
                return redirect('signup')
             user=User.objects.create_user(username=email,password=password)
             user.save()
             print('user Created')
             return redirect('signin')
       else:
          messages.info("password not match")
          return redirect('signup')
       return redirect('/')
    return render(request,"signup.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

def forum(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        state = request.POST.get('state')
        district = request.POST.get('district')
        Account1 = request.POST.get('Account1')
        Debit = request.POST.get('Debit')
        Credit = request.POST.get('Credit')
        Cheque = request.POST.get('Cheque')


        newplace1= newplace (name=name, dob=dob, age=age, gender=gender, mobile=mobile, phone=phone, email=email,
                                address=address, state=state, district=district,  Account1=Account1, Debit=Debit,
                                Credit=Credit, Cheque=Cheque)

        if newplace1 is not None:
         newplace1.save()
         messages.success(request, 'Application Accepted')
         return redirect("/forum")

        else:
            messages.info(request, "invalid credentials")
    return render(request,"forum.html")
