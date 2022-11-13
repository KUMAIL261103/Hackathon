from django.urls import path 
from . import views

urlpatterns=[
    path('',views.home_new,name='home_new'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('studenthome',views.studenthome,name='studenthome'),
    path('logout',views.logout,name='logout'),
    path('page2',views.page2,name='page'),
    path('page1',views.page1,name='page1'),
    path('personalinfo',views.personalinfo,name='personalinfo'),
    path('company',views.company,name='company'),
    path('company2',views.company2,name='COMPANY2'),
    path('company3',views.company3,name='COMPANY3'),
    path('company4',views.company4,name='COMPANY4'),
    path('company5',views.company5,name='COMPANY5'),
    path('company6',views.company6,name='COMPANY6')
]