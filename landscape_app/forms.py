from django import forms
from .models import *

class Companyregform(forms.Form):
    companyname = forms.CharField(max_length=50)
    country = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    district = forms.CharField(max_length=50)
    zipcode = forms.IntegerField()
    address = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(max_length=20)
    cpassword = forms.CharField(max_length=20)
    phone = forms.IntegerField()

class Comapnyloginform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)

# class Userregform(forms.ModelForm):
#     class Meta:
#         model=Userregmodel
#         fields='__all__'
#
# class Userloginform(forms.Form):
#     email=forms.EmailField()
#     password=forms.CharField(max_length=20)




class Userregform(forms.Form):
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    fullname = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    country = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    district = forms.CharField(max_length=50)
    zipcode = forms.IntegerField()
    address = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(max_length=20)
    cpassword = forms.CharField(max_length=20)
    phone = forms.IntegerField()

class Userloginform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)



class AddServicesForm(forms.Form):
    companyname = forms.CharField(max_length=50)
    services=forms.CharField(max_length=300)
    address = forms.CharField(max_length=150)
    email=forms.EmailField()
    phone = forms.IntegerField()


class Bookserviceform(forms.Form):
    fullname = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.IntegerField()
    address = forms.CharField(max_length=300)
    companyname = forms.CharField(max_length=50)
    service = forms.CharField(max_length=50)



class Addprojectsform(forms.Form):
    companyname=forms.CharField(max_length=50)
    location=forms.CharField(max_length=100)
    Description=forms.CharField(max_length=150)
    image=forms.FileField()