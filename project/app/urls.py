from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login),
    path('register',views.register),
    path('employeeselfview/<data>',views.employeeselfview),
    path('update_emp/<pk>',views.update_emp),
    path('delete/<pk>',views.delete)
]