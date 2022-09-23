from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver #add this
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,blank=True)
    roll = models.CharField(default='insure',max_length=255)
    email = models.EmailField()
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

class Insure(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,blank=True)
    adhar = models.CharField(max_length=255,blank=True)
    adhar_mobile = models.CharField(max_length=255,blank=True)
    email = models.CharField(max_length=255,blank=True)
    dob = models.CharField(max_length=255,blank=True)
    father_name = models.CharField(max_length=255,blank=True)
    mother_name = models.CharField(max_length=255,blank=True)
    address = models.CharField(max_length=255,blank=True)
    status = models.CharField(max_length=255,blank=True)
    spouse = models.CharField(max_length=255,blank=True)
    qulification = models.CharField(max_length=255,blank=True)
    pob = models.CharField(max_length=255,blank=True)
    pan = models.CharField(max_length=255,blank=True)
    occupation = models.CharField(max_length=255,blank=True)
    AIncome = models.CharField(max_length=255,blank=True)
    Employer = models.CharField(blank=True,max_length=255)
    service = models.CharField(max_length=255,blank=True)

    # block chain
    new_hash = models.CharField(max_length=500,default='')
    created = models.DateField(auto_now_add=True)

    app_status = models.CharField(max_length=255,default='Pending')
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

class Provider(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    service = models.CharField(max_length=255)
    hospital = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    email = models.EmailField()

    ENT = models.FileField(upload_to='doc/')
    ED = models.FileField(upload_to='doc/')
    AT = models.FileField(upload_to='doc/')
    HI = models.FileField(upload_to='doc/')

    
    new_hash = models.CharField(max_length=500,default='')
    created = models.DateField(auto_now_add=True,)


    insurence = models.ManyToManyField(Insure,blank=True)

    class Meta:
        ordering = ['-id']