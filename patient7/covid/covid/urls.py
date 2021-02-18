from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.indexpage),
    path('signup_patient/',views.signup_patient_page, name="signupp"),
    path('login_patient/',views.login_patient_page, name="loginp"),
    path('patient_profile/<int:patient_id>',views.patient_profile_page, name="patientprofile"),
    path('logout_patient/', views.patient_logout, name="logoutp"),
    path('signup_doctor/',views.signup_doctor_page, name="signupd"),
    path('login_doctor/',views.login_doctor_page, name="logind"),
    path('doctor_profile/<int:doctor_id>',views.doctor_profile_page),
  
]
