from django.urls import path
from . import views

urlpatterns = [

    #Login and Registration
    path('',views.login),
    path('register',views.register),
    path('logout',views.logout),
    
    #Employee Section
    path('employeeselfview',views.employeeselfview),
    path('update_emp',views.update_emp),
    path('delete',views.delete),
    path('frgtpsw',views.frgtpsw),
    
    #Admin Section
    path('admin_home',views.admin_home),
    path('view_employee',views.view_employee),
    path('add_work',views.add_work),
    path('new_request',views.new_request),
    path('activate_emp/<pk>',views.activate_emp),
    
]