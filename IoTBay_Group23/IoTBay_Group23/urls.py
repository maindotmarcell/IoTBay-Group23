"""IoTBay_Group23 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from main import views as v
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"),
    path('', include("main.urls")),
    path('home/', v.home, name="home"),
    path('', include("django.contrib.auth.urls")),
    path('welcome/', v.welcome, name="welcome"),
    path('main/', v.main, name="main"),
    path('logout/', v.logout, name="logout"),
    path('edit/', v.edit, name="edit"),
    path('registration/', include('django.contrib.auth.urls')),

    #reset password path
    path('resetpassword/', auth_views.PasswordResetView.as_view(template_name='registration/resetpassword.html'), name = "reset_password"),
    path('resetpasswordsent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/resetpasswordsent.html'), name = "password_reset_done"),
    path('<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/resetpasswordform.html'), name = "password_reset_confirm"),
    path('resetpasswordcomplete', auth_views.PasswordResetCompleteView.as_view(template_name='registration/resetpassworddone.html'), name = "password_reset_complete"),


    #path('resetpassword', v.reset_password_form, name="reset_password_form")

]

# /home/start
