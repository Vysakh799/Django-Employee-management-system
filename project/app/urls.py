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
    path('frgtpsw',views.frgtpsw),
    
    #Admin Section
    path('admin_home',views.admin_home),
    path('view_employee',views.view_employee),
    path('add_wrok',views.add_work),
    path('new_request',views.new_request),
    
]