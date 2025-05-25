from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from .models import Notification
from django.http import JsonResponse

# Create your views here.

def index(request):
    # return HttpResponse("Hello world")
    # return render(request, "Home/index.html")
    return render(request, "authentication/login.html")
def dashboard(request):

    unread_notification = Notification.objects.filter(user=request.user, is_read=False)
    unread_notification_count = unread_notification.count()

    return render(request, "students/student-dashboard.html")


def mark_notification_as_read(request):
    if request.method == 'POST':
        notification = Notification.objects.filter(user=request.user, is_read=False)
        notification.update(is_read=True)
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden()

def clear_all_notification(request):
    if request.method == 'POST':
        notification = Notification.objects.filter(user=request.user)
        notification.delete()
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden()



