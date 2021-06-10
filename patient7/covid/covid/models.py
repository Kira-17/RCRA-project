from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User
# from simple_history import register
# register(User)


class doctor(models.Model):
    
    full_name=models.CharField(max_length=100)
    hospital_name=models.CharField(max_length=100)
    number_doc=models.CharField(max_length=10)
    # doc_id=models.IntegerField()
    
    user_doc=models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user_doc.username
    

class patient(models.Model):
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    patient_id=models.CharField(max_length=10, null=True)
    address=models.CharField(max_length=100)
    number=models.CharField(max_length=10)
    emergency_number=models.CharField(max_length=10)
    age=models.IntegerField()
    health_condition=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    alternate_email=models.CharField(max_length=100)
    
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    doctorw=models.ForeignKey(doctor, on_delete=models.CASCADE, null=True, related_name="help")

    def __str__(self):
        return self.user.username


class patientsymptoms(models.Model):
    btemp=models.IntegerField()
    sympt1=models.CharField(max_length=100,null=False)
    patient_fkey=models.ForeignKey(patient,on_delete=models.CASCADE,null=True)
    history=HistoricalRecords()
    # log= HistoricalRecords(related_name='history')

    def __str__(self):
        return self.patient_fkey.name



