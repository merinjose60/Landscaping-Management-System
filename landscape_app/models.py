from django.db import models

# Create your models here.
class Companyregmodel(models.Model):
    catchoice1 = [
        ('India', 'India'),
        ('UAE', 'UAE')
    ]
    catchoice2 = [
        ('Kerala', 'Kerala'),
        ('Dubai', 'Dubai')
    ]
    catchoice3 = [
        ('Alappuzha', 'Alappuzha'),
        ('Al-Karama', 'Al-Karama'),
        ('Bur Dubai', 'Bur Dubai'),
        ('Deira', 'Deira'),
        ('Ernakulam', 'Ernakulam'),
        ('Idukki', 'Idukki'),
        ('Kannur', 'Kannur'),
        ('Kasaragod', 'Kasaragod'),
        ('Kollam', 'Kollam'),
        ('Kottayam', 'Kottayam'),
        ('Kozhikode', 'Kozhikode'),
        ('Malappuram', 'Malappuram'),
        ('Palakkad', 'Palakkad'),
        ('Pathanamthitta', 'Pathanamthitta'),
        ('Palakkad', 'Palakkad'),
        ('Thrissur', 'Thrissur'),
        ('Thiruvanathapuram', 'Thiruvanathapuram'),
        ('Wayanad', 'Wayanad')
    ]

    companyname = models.CharField(max_length=50)
    country = models.CharField(max_length=50, choices=catchoice1)
    state = models.CharField(max_length=50, choices=catchoice2)
    district = models.CharField(max_length=50, choices=catchoice3)
    zipcode = models.IntegerField()
    address = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone = models.BigIntegerField()


class Userregmodel(models.Model):
    catchoice1 = [
        ('India', 'India'),
        ('UAE', 'UAE')
    ]
    catchoice2 = [
        ('Kerala', 'Kerala'),
        ('Dubai', 'Dubai')
    ]
    catchoice3 = [
        ('Alappuzha', 'Alappuzha'),
        ('Al-Karama','Al-Karama'),
        ('Bur Dubai', 'Bur Dubai'),
        ('Deira', 'Deira'),
        ('Ernakulam', 'Ernakulam'),
        ('Idukki', 'Idukki'),
        ('Kannur', 'Kannur'),
        ('Kasaragod', 'Kasaragod'),
        ('Kollam', 'Kollam'),
        ('Kottayam', 'Kottayam'),
        ('Kozhikode', 'Kozhikode'),
        ('Malappuram', 'Malappuram'),
        ('Palakkad', 'Palakkad'),
        ('Pathanamthitta', 'Pathanamthitta'),
        ('Palakkad', 'Palakkad'),
        ('Thrissur', 'Thrissur'),
        ('Thiruvanathapuram', 'Thiruvanathapuram'),
        ('Wayanad', 'Wayanad')
    ]

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    country = models.CharField(max_length=50, choices=catchoice1)
    state = models.CharField(max_length=50, choices=catchoice2)
    district = models.CharField(max_length=50, choices=catchoice3)
    zipcode = models.IntegerField()
    address = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone = models.BigIntegerField()



class AddServicesModel(models.Model):
    companyname = models.CharField(max_length=50)
    services = models.CharField(max_length=300)
    address = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.BigIntegerField()

class Bookservicemodel(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.BigIntegerField()
    address = models.CharField(max_length=300)
    companyname = models.CharField(max_length=50)
    service = models.CharField(max_length=50)



class Addtowishlistmodel(models.Model):
    companyname = models.CharField(max_length=50)
    services = models.CharField(max_length=300)
    address = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.BigIntegerField()





class Addprojectsmodel(models.Model):
    companyname=models.CharField(max_length=50)
    location=models.CharField(max_length=100)
    Description=models.CharField(max_length=150)
    image=models.FileField(upload_to='landscape_app/static')

