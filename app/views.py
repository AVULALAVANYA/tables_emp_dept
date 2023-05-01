from django.shortcuts import render
from app.models import *
# Create your views here.
def insert_emp(request):
    LOW=employe.objects.all()
    d={'emp':LOW}
    return render(request,'insert_emp.html',d)
def insert_dept(request):
    LOW=department.objects.all()
    d={'dept':LOW}
    return render(request,'insert_dept.html',d)