from django.urls import path
from . import views

urlpatterns = [

    #Login and Registration
    path('',views.login),
    path('register',views.register),
    
    #Employee Section
    path('employeeselfview/<data>',views.employeeselfview),
    path('update_emp/<pk>',views.update_emp),
    path('delete/<pk>',views.delete),
    path('employee_home',views.employee_home),
    #Admin Section
    path('admin_home',views.admin_home),
    
]