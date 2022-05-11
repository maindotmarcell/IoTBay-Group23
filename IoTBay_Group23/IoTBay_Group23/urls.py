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
from django.conf.urls.static import static
from django.conf import settings

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
    path('confirmation/', v.confirmation, name="confirmation"),
    path('deleteaccount/', v.DeleteAccount, name="deleteaccount"),
    path('cart/', v.cart, name="cart"),   
    path('checkout/', v.checkout, name="checkout"),
    path('registration/', include('django.contrib.auth.urls')),


    # update item json view
    path('update_item/', v.updateItem, name="update_item"),

    #staff registration
    path('staff_registration/', v.staff_registration, name="staff_Registration"),

    #reset password path
    path('resetpassword/', auth_views.PasswordResetView.as_view(template_name='registration/resetpassword.html'), name = "reset_password"),
    path('resetpasswordsent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/resetpasswordsent.html'), name = "password_reset_done"),
    path('<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/resetpasswordform.html'), name = "password_reset_confirm"),
    path('resetpasswordcomplete', auth_views.PasswordResetCompleteView.as_view(template_name='registration/resetpassworddone.html'), name = "password_reset_complete"),

    #payment management path
    path('edit_payment/', v.edit_payment, name="edit_payment"),
    path('delete_payment/', v.delete_payment, name="delete_payment"),
    path('delete_payment_confirmation/', v.delete_payment_confirmation, name='delete_payment_confirmation'),

    #path('resetpassword', v.reset_password_form, name="reset_password_form")

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# /home/start
