from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def login(request):
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        phno=request.POST['phno']
        nm=name[:3]
        ph=str(phno[:3])
        emp_id=nm+ph
        address=request.POST['address']
        username=request.POST['username']
        password=request.POST['password']
        data=employee.objects.create(emp_id=emp_id,name=name,age=age,email=email,phno=phno,address=address,username=username,password=password)
        data.save()
        return redirect(login)
    else:
        return render(request,'register.html')