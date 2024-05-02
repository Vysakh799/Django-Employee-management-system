from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        try:
            data=employee.objects.get(username=username,password=password)
            return render(request,'employee_self_view.html',{'data':data})
        #     # return HttpResponse('successfull')
        except:
            # return HttpResponse('loggedin')
            return HttpResponse('Invalid Username or password')    
    else:
        return render(request,"login.html")
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
        try:
            data=employee.objects.get(username=username)
            return HttpResponse('Username exist')
        except:
            pass
        password=request.POST['password']
        data=employee.objects.create(emp_id=emp_id,name=name,age=age,email=email,phno=phno,address=address,username=username,password=password)
        data.save()
        return redirect(login)
    else:
        return render(request,'register.html')
def employeeselfview(request,data):
    data=employee.objects.get(pk=data)
    return render(request,'employee_self_view.html',{'data':data})
def update_emp(request,pk):
    data=employee.objects.get(pk=pk)
    emp=data
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        phno=request.POST['phno']
        address=request.POST['address']
        data=employee.objects.filter(pk=pk).update(name=name,age=age,email=email,phno=phno,address=address)
        return redirect('../employeeselfview/{}'.format(data))
    return render(request,'update_emp.html',{'emp':emp})
def delete(request,pk):
    employee.objects.filter(pk=pk).delete()
    return redirect(login)