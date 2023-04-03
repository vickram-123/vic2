from django.shortcuts import render
from .forms import studentRegistration
# Create your views here.
def showformdata(r):
    fm = studentRegistration()
    return render(r,'enroll/userregistration.html',
                  {'form':fm})