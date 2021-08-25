from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'kingsForms/home.html')
    return HttpResponse("<center style='background-color: lightgrey'><h1>Thank you for contacting me! </h1></center>")