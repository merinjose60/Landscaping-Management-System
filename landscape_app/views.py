import os

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from dream_pro.settings import EMAIL_HOST_USER


from .forms import *
from .models import *


def indexpage(request):
    return render(request, 'index.html')


def userprofile(request):
    return render(request, 'userprofile.html')


def companyprofile(request):
    return render(request, 'companyprofile.html')
def contactus(request):
    return render(request, 'contact.html')

def aboutus(request):
    return render(request, 'about.html')

def gallery(request):
    a = Addprojectsmodel.objects.all()
    b = Bookservicemodel.objects.all()
    im = []
    cn = []
    loc = []
    des = []
    id1 = []
    for i in a:
        id = i.id
        id1.append(id)
        img = i.image
        im.append(str(img).split('/')[-1])
        cmp = i.companyname
        cn.append(cmp)
        lo = i.location
        loc.append(lo)
        de = i.Description
        des.append(de)
    mylist = zip(im, cn, loc, des, id1)
    return render(request, 'gallery.html', {'a': mylist, 'b': b})

def companyregister(request):
    if request.method == 'POST':
        a = Companyregform(request.POST)
        if a.is_valid():
            cn = a.cleaned_data['companyname']
            c = a.cleaned_data['country']
            s = a.cleaned_data['state']
            d = a.cleaned_data['district']
            zc = a.cleaned_data['zipcode']
            add = a.cleaned_data['address']
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            cp = a.cleaned_data['cpassword']
            ph = a.cleaned_data['phone']

            if ps == cp:
                b = Companyregmodel(companyname=cn, country=c, state=s, district=d,
                                    zipcode=zc, address=add, email=em, password=ps, phone=ph)
                b.save()
                return redirect(companylogin)
            else:
                return HttpResponse("Incorrect password")
        else:
            return HttpResponse("registration failed")
    else:
        return render(request, 'companyregister.html')


def companylogin(request):
    if request.method == 'POST':
        a = Comapnyloginform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = Companyregmodel.objects.all()
            for i in b:
                cmp = i.companyname
                request.session['companyname']=cmp
                id = i.id
                if i.email == em and i.password == ps:
                    return render(request, 'companyprofile.html', {'cmp': cmp, 'id': id})
        else:
            return HttpResponse("Login Failed")
    else:
        return render(request, 'companylogin.html')
def userregister(request):
    if request.method == 'POST':
        a = Userregform(request.POST)
        if a.is_valid():
            fn = a.cleaned_data['firstname']
            ln = a.cleaned_data['lastname']
            fna = a.cleaned_data['fullname']
            un = a.cleaned_data['username']
            c = a.cleaned_data['country']
            s = a.cleaned_data['state']
            d = a.cleaned_data['district']
            zc = a.cleaned_data['zipcode']
            add = a.cleaned_data['address']
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            cp = a.cleaned_data['cpassword']
            ph = a.cleaned_data['phone']

            if ps == cp:
                b = Userregmodel(firstname=fn, lastname=ln, fullname=fna, username=un, country=c, state=s, district=d,
                                    zipcode=zc, address=add, email=em, password=ps, phone=ph)
                b.save()
                return redirect(userlogin)
            else:
                return HttpResponse("Incorrect password")
        else:
            return HttpResponse("registration failed")
    else:
        return render(request, 'userregister.html')

def userlogin(request):
    if request.method == 'POST':
        a = Userloginform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = Userregmodel.objects.all()
            for i in b:
                fn = i.fullname
                request.session['fullname']=fn
                request.session['email']=em
                id = i.id
                if i.email == em and i.password == ps:
                    return render(request, 'userprofile.html', {'fn': fn,'em':em, 'id': id})
        else:
            return HttpResponse("Login Failed")
    else:
        return render(request, 'userlogin.html')


# Add Services

def addservices(request,id):
    readonly = Companyregmodel.objects.get(id=id)
    cn = readonly.companyname
    em = readonly.email
    add = readonly.address
    ph = readonly.phone
    if request.method == 'POST':
        a = AddServicesForm(request.POST)
        if a.is_valid():
            cn = a.cleaned_data['companyname']
            s = a.cleaned_data['services']
            add = a.cleaned_data['address']
            em=a.cleaned_data['email']
            ph = a.cleaned_data['phone']
            b = AddServicesModel(companyname=cn, services=s, address=add, email=em, phone=ph)
            b.save()
            return redirect(addservicesdisplay)
        else:
            return HttpResponse("Add Service Uploading Failed")

    else:
        return render(request, 'addservices.html', {'cn': cn, 'em': em, 'ph':ph,'add':add})

def addservicesdisplay(request):
    x = AddServicesModel.objects.all()
    b = request.session['companyname']
    return render(request,'addservicesdisplay.html',{'a': x,'b':b})

def editaddservice(request,id):
    a = AddServicesModel.objects.get(id=id)
    if request.method == 'POST':
        a.companyname = request.POST.get('companyname')
        a.services = request.POST.get('services')
        a.address = request.POST.get('address')
        a.email = request.POST.get('email')
        a.phone = request.POST.get('phone')
        a.save()

        return redirect(addservicesdisplay)
    return render(request, 'editaddservice.html', {'a': a})

def addservicedelete(request, id):
    a = AddServicesModel.objects.get(id=id)
    a.delete()
    return redirect(addservicesdisplay)

def viewbookservice(request):
    a=AddServicesModel.objects.all()
    return render(request,'viewbookservice.html',{'a':a})

def bookservice(request,id):
    b = AddServicesModel.objects.get(id=id)
    cn = b.companyname
    if request.method == 'POST':
        a = Bookserviceform(request.POST)
        if a.is_valid():
            fn=a.cleaned_data['fullname']
            add = a.cleaned_data['address']
            ph = a.cleaned_data['phone']
            em = a.cleaned_data['email']
            s = a.cleaned_data['service']
            cn = a.cleaned_data['companyname']
            c = Bookservicemodel(companyname=cn, service=s, phone=ph, fullname=fn, email=em, address=add)
            c.save()
            subject = f"Booking Successful - {cn}"
            messege = f"Hi {fn}\nYour booking for {cn} services is successful, we will reach you to discuss further proceedings with your booking"
            send_mail(subject, messege, EMAIL_HOST_USER, [em])

            return redirect(displaymybookings)
        else:
            return HttpResponse("Booking Failed")
    else:
        return render(request, 'bookservice.html', {'cn': cn})


def bookingconfirmation(request,id):
    b=Bookservicemodel.objects.get(id=id)
    cn=b.companyname
    fn=b.fullname
    ser=b.service
    em=b.email
    subject = f"{cn} - Booking Confirmation Mail"
    messege = f"Hi {fn}\n  Greetings from {cn} your booking for {ser} is confirmed we will contact you soon "
    send_mail(subject, messege, EMAIL_HOST_USER, [em])
    return redirect(bookingemailalert)


def bookingemailalert(request):
    return render(request, 'bookingservicealert.html')

def viewregisteredcompanies(request):
    x = Companyregmodel.objects.all()
    return render(request, 'viewregisteredcompanies.html', {'a':x})
def displaymybookings(request):
    a = AddServicesModel.objects.all()
    c = Bookservicemodel.objects.all()
    b = request.session['fullname']
    return render(request, 'displaymybookings.html', {'a':a,'b':b,'c':c})
def viewbookedusers(request):
    a = Bookservicemodel.objects.all()
    b = request.session['companyname']
    return render(request,'viewbookedusers.html',{'a':a,'b':b})


def wishlist(request, id):
    a = AddServicesModel.objects.get(id=id)
    b = Addtowishlistmodel(companyname=a.companyname, services=a.services, address=a.address, email=a.email, phone=a.phone)
    b.save()
    return redirect(wishlistdisplay)

def wishlistdisplay(request):
    x = Addtowishlistmodel.objects.all()
    b = request.session['fullname']
    return render(request, 'wishlistdisplay.html', {'a': x,'b':b})


def wishlistdelete(request,id):
    a = Addtowishlistmodel.objects.get(id=id)
    a.delete()
    return redirect(wishlistdisplay)





def addprojects(request,id):
    readonly = Companyregmodel.objects.get(id=id)
    cn = readonly.companyname
    if request.method == 'POST':
        a = Addprojectsform(request.POST,request.FILES)
        if a.is_valid():
            cmp = a.cleaned_data['companyname']
            loc = a.cleaned_data['location']
            des = a.cleaned_data['Description']
            im = a.cleaned_data['image']
            b = Addprojectsmodel(companyname=cmp, location=loc, Description=des, image=im)
            b.save()

            return redirect(addprojectsdisplay)
        else:
            return HttpResponse("Add Projects Uploading Failed")

    else:
        return render(request, 'addprojects.html', {'cn': cn})


def addprojectsdisplay(request):
    a = Addprojectsmodel.objects.all()
    b = request.session['companyname']
    im=[]
    cn = []
    loc = []
    des = []
    id1 = []
    for i in a:
        id = i.id
        id1.append(id)
        img = i.image
        im.append(str(img).split('/')[-1])
        cmp = i.companyname
        cn.append(cmp)
        lo = i.location
        loc.append(lo)
        de = i.Description
        des.append(de)
    mylist = zip(im, cn, loc, des, id1)
    return render(request, 'addprojectsdisplay.html', {'a': mylist, 'b': b})


def viewprojects(request):
    a = Addprojectsmodel.objects.all()
    b = Bookservicemodel.objects.all()
    im = []
    cn = []
    loc = []
    des = []
    id1 = []
    for i in a:
        id = i.id
        id1.append(id)
        img = i.image
        im.append(str(img).split('/')[-1])
        cmp = i.companyname
        cn.append(cmp)
        lo = i.location
        loc.append(lo)
        de = i.Description
        des.append(de)
    mylist = zip(im, cn, loc, des, id1)
    return render(request, 'viewprojects.html', {'a': mylist,'b':b})

def editprojects(request,id):
    a=Addprojectsmodel.objects.get(id=id)
    image=str(a.image).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES) !=0:
            if len(a.image) >0:
                os.remove(a.image.path)
            a.image=request.FILES['newimage']
        a.companyname=request.POST.get('companyname')
        a.location=request.POST.get('location')
        a.Description=request.POST.get('Description')
        a.save()
        return redirect(addprojectsdisplay)
    return render(request,'editproject.html',{'a':a,'image':image})



def deleteproject(request,id):
    a=Addprojectsmodel.objects.get(id=id)
    if len(a.image)>0:
        os.remove(a.image.path)
    a.delete()
    return redirect(addprojectsdisplay)