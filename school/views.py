from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("Hello world")
    # return render(request, "Home/index.html")
    return render(request, "authentication/login.html")
def dashboard(request):
    return render(request, "students/student-dashboard.html")