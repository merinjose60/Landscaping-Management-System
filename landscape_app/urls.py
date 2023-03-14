from django.urls import path
from .views import *

urlpatterns = [
    path('index/',indexpage),
    path('userprofile/',userprofile),
    path('companyprofile/',companyprofile),
    path('companyregister/', companyregister),
    path('companylogin/', companylogin),
    path('userregister/',userregister),
    path('userlogin/',userlogin),
    path('addservice/<int:id>/', addservices),
    path('addservicesdisplay/', addservicesdisplay),
    path('editaddservice/<int:id>',editaddservice),
    path('deleteaddservice/<int:id>',addservicedelete),
    path('viewbookservice/', viewbookservice),
    path('bookservice/<int:id>/',bookservice),
    path('bookingconfirmation/<int:id>',bookingconfirmation),
    path('bookingemailalert/',bookingemailalert),

    path('viewregisteredcompanies/',viewregisteredcompanies),

    path('viewbookedusers/',viewbookedusers),

    path('wishlist/<int:id>',wishlist),
    path('wishlistdisplay/',wishlistdisplay),
    path('wishlistdelete/<int:id>',wishlistdelete),

    path('displaymybookings/',displaymybookings),

    path('addprojects/<int:id>/', addprojects),
    path('addprojectsdisplay/', addprojectsdisplay),
    path('editproject/<int:id>',editprojects),
    path('deleteproject/<int:id>',deleteproject),
    path('viewprojects/',viewprojects),
    path('gallery/',gallery),
    path('contactus/',contactus),
    path('aboutus/',aboutus)
]