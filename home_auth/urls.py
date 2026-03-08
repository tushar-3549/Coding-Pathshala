
from django.contrib import admin
from django.urls import path, include
from .views import *

# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('forgot-password/', forgot_password_view, name='forgot-password'),
    path('reset-password/<str:token>/', reset_password_view, name='reset_password'),
    path('logout/', logout_view, name='logout'),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)