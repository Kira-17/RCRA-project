from django.contrib import admin
from .models import patient
from .models import doctor,patientsymptoms
from simple_history import register

admin.site.register(patient)
admin.site.register(doctor)
admin.site.register(patientsymptoms)


