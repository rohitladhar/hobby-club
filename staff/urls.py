from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns=[
            path('',views.login,name="login"),
            path('homepage',views.homepage,name="homepage"),
            path('forget',views.forget,name="forget"),
            path('userlogin',views.userlogin,name="userlogin"),
            path('logout',views.logout,name="logout"),
            path('booking',views.booking,name="booking"),    
            path('addcontent',views.addcontent,name="addcontent"),
            path('addrecord',views.addrecord,name="addrecord"),
            path('seatbooking',views.seatbooking,name="seatbooking"),
            path('deletebooking',views.BookingListView.as_view(),name="deletebooking"),
            path('bookingdelete/<int:pk>',views.bookingdelete,name="bookingdelete"),
            #path('applicationview',views.applicationview,name="applicationview"),
            #path('contentview',views.contentview,name="contentview"),
            #path('recordview',views.recordview,name="recordview"),
            path('recordview',views.RecordListView.as_view(),name="recordview"),
            path('contentview',views.ContentListView.as_view(),name="contentview"),
            path('applicationview',views.ApplicationListView.as_view(),name="applicationview"),
            path('recordaddition',views.recordaddition,name="recordaddition"),
            path('contentaddition',views.contentaddition,name="contentaddition"),
            path('applicationupdate/<int:pk>',views.applicationupdate,name="applicationupdate"),
            path('applicationupdate/applicationupdate',views.updateapplication,name="applicationupdate/applicationupdate"),
            path('contentupdate/<int:pk>',views.contentupdate,name="contentupdate"),
            path('contentupdate/contentupdate',views.updatecontent,name="contentupdate/contentupdate"),
            path('recordupdate/<int:pk>',views.recordupdate,name="recordupdate"),
            path('recordupdate/recordupdate',views.updaterecord,name="recordupdate/recordupdate"),
            path('bookingview',views.bookingview,name="bookingview"),
            path('bookinglist',views.bookinglist,name="bookinglist"),
            path('contact',views.ContactListView.as_view(),name="contact"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
