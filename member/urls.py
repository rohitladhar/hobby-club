from django.urls import path
from . import views

urlpatterns=[
            path('',views.index,name="index"),
            path('login',views.login,name="login"),
            path('index',views.index,name="index"),
            path('userlogin',views.userlogin,name="userlogin"),
            path('memberhome',views.memberhome,name="memberhome"),
            path('logout',views.logout,name="logout"),
            path('articleview/<int:pk>',views.articleview,name="articleview"),
            path('article',views.article,name="article"),
            path('memberbooking',views.memberbooking,name="memberbooking"),
            path('seatchecking',views.seatchecking,name="seatchecking"),
            path('checkbooking/confirmbooking',views.confirmbooking,name="confirmbooking"),
            path('checkbooking/<str:slot>',views.checkbooking,name="checkbooking"),
            path('checkbooking/checkbooking/bookingseat',views.bookingseat,name="bookingseat"),
            path('updatepassword',views.updatepassword,name="updatepassword"),
            path('updatedetail',views.updatedetail,name="updatedetail"),
            path('discussion',views.discussion,name="discussion"),
            path('contactus',views.contactus,name="contactus"),
]

