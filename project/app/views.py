from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages


#Logging and Registration

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        try:
            data=employee.objects.get(username=username,password=password)
            if data.status=='active':
                request.session['user']=username
                return redirect(employeeselfview)
            else:
                messages.success(request,"Approval Pending")
                return redirect(login)  

        #     # return HttpResponse('successfull')
        except:
            # return HttpResponse('loggedin')
            if username=='admin123' and password=='admin@123':
                request.session['admin']=username
                return redirect(admin_home)
            else:
                messages.success(request,"Invalid Username")  
                return redirect(login)  
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
        password=request.POST['password']
        status='deactive'
        try:
            data=employee.objects.get(username=username)
            messages.success(request,"Username Exist")  
            return redirect(register)
        except:
            data=employee.objects.create(emp_id=emp_id,name=name,age=age,email=email,phno=phno,address=address,username=username,password=password,status=status)
            data.save()
            messages.success(request,"Approval Pending")  


        
        return redirect(login)
    else:
        return render(request,'register.html')

def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return redirect(login)
    elif 'admin' in request.session:
        del request.session['admin']
        return redirect(login)
    else:
        return redirect(login)
    

#Admin Section


def admin_home(request):
    if 'admin' in request.session:
        return render(request,'admin_template/admin_home.html')
    else:
        return redirect(login)
def view_employee(request):
    data=employee.objects.all()
    return render(request,'admin_template/view_employee.html',{'data':data})
def new_request(request):
    data=employee.objects.filter(status='deactive')

    return render(request,'admin_template/new_request.html',{'data':data})
def add_work(request):
    return render(request,'admin_template/add_work.html')
def activate_emp(request,pk):
    employee.objects.filter(pk=pk).update(status='active')
    messages.success(request,"Approval successfull")  

    return redirect(new_request)






#Employee Section



def employeeselfview(request):
    if 'user' in request.session:
        data=employee.objects.get(username=request.session['user'])

        return render(request,'employee_template/employee_self_view.html',{'data':data})
    else:
        return redirect(login)
    
def update_emp(request):
    if 'user' in request.session:
        data=employee.objects.get(username=request.session['user'])
        emp=data
        if request.method=='POST':
            name=request.POST['name']
            age=request.POST['age']
            email=request.POST['email']
            phno=request.POST['phno']
            address=request.POST['address']
            data=employee.objects.filter(username=request.session['user']).update(name=name,age=age,email=email,phno=phno,address=address)
            return redirect(employeeselfview)
        return render(request,'employee_template/update_emp.html',{'emp':emp})
    else:
        return redirect(login)
def delete(request):
    if 'user' in request.session:
        employee.objects.filter(username=request.session['user']).delete()
        del request.session['user']

    return redirect(login)

#Employee frgt password section
def frgtpsw(request):
    if request.method=="POST":
        username=request.POST['username']
        n_password=request.POST['n_password']
        c_password=request.POST['c_password']
        try:
            data=employee.objects.get(username=username)
            if n_password==c_password:
                employee.objects.filter(username=username).update(password=c_password)
            else:
                messages.success(request,"Passwords Doesn't match") 
                return redirect(frgtpsw)
        except:
            messages.success(request,"Invalid Username") 
            return redirect(frgtpsw)
        return redirect(login)
        


    else:
        return render(request,'employee_template/frgtpsw.html')