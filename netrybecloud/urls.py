from django.urls import path
from.import views
urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about, name='about'),
    path('training/',views.training, name='courses'),
    path('coursedetails/',views.coursesdetails,name='coursedets'),
    path('contact/', views.contact, name='contact'),
    path('datasci/',views.datasci,name='datasci'),
    path('frontend/',views.frontend,name='frontend'),
    path('productdesign/',views.productdesign,name='productdesign'),
    path('backend/',views.backend, name='backend'),
    path('schprog/', views.schprog, name='schprog'),
    path('aftersch/', views.aftersch, name='aftersch'),
    path('workshop/', views.workshop, name='workshop'),
    path('nimblyprogram/', views.nimbly, name='nimblyprog'),
    path('softwaredev/', views.software, name='softwaredev'),
    path('BI/', views.business, name='business'),
    path('enterprise/', views.entreprise, name='enterprise'),
    path('hustle-biz/', views.entreprise, name='hustle')
]