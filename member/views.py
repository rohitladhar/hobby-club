from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User,auth,Group
from django.contrib import messages
from .models import UserLogin
from staff.models import Records,Content,Booking
from .models import Application,Contactus
from django.db.models import Q
from django.contrib import messages
def index(request):
    return render(request,"index.html")

    
def membername(request):
    username = request.session.get('username', 'username')
    record=Records.object.get(username=username)
    user=UserLogin.object.get(username=username)
    
    context={
        'record':record,
        'user':user
    }
    return context

def login(request):
    return render(request,"login.html")

def memberhome(request):
    context=membername(request)
    return render(request,"member/index.html",context)

def discussion(request):
    context=membername(request)
    return render(request,"member/discussion.html",context)

def contactus(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        email=request.POST['email']
        desc=request.POST['desc']
        group=request.POST['group']
        
        contact=Contactus(fname=fname,group=group,lname=lname,desc=desc,phone=phone,email=email)
        contact.save()
        message='Your form is submitted successfully. Our customer care executive will contact you very soon. '
        context={
            'message':message
        }
        return render(request,"contact.html",context)

def userrecord(request,username):
    record=Records.object.get(username=username)
    user=UserLogin.object.get(username=username)
    request.session['username']=username
    request.session['group']=record.group
    context={
        'record':record,
        'user':user
    }
    return render(request,"member/index.html",context)

def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        if UserLogin.objects.filter(Q(username=username),Q(password=password)).exists():
            if Records.object.filter(Q(username=username),Q(status='Active')):
                username=userrecord(request,username)
                return username
            else:
                user_warning="Your are not allowed to login-in"
                context={
                    'user_warning':user_warning
                }
                return render(request,"inactive.html",context)
            
        else:
            messages.info(request,'Invalid user credentials')
            return render(request,"login.html")

def logout(request):
    del request.session['username']
    return redirect('index')

def article(request):
    context=membername(request)
    group = request.session.get('group', 'group')
    articles=Content.objects.filter(group=group)
    select='Select Articles from dropdown'
    newcontent={
        'context':context,
        'articles':articles,
        'select':select
    }
    return render(request,"member/article.html",newcontent)

#def articlehome(request):
#   return redirect('article')

def articleview(request,pk):
    context=membername(request)
    description=Content.object.get(pk=pk)
    group = request.session.get('group', 'group')
    articles=Content.objects.filter(group=group)
    context={
        'description':description,
        'context':context,
        'articles':articles
    }
    return render(request,"member/article.html",context)
    
def memberbooking(request):
    context=membername(request)
    select="Select Slot from dropdown"
    newcontent={
        'select':select,
        'context':context
    }
    return render(request,"member/checkbooking.html",newcontent)

def checkbooking(request,slot):
    context=membername(request)
    group = request.session.get('group', 'group')
    
    if Booking.object.filter(Q(group=group),Q(slot=slot)).exists():
        booking=Booking.object.get(Q(group=group),Q(slot=slot))
        available=booking.available
        booked=booking.booked
        date=booking.date
        theme=booking.theme
        newcontent={
            'available':available,
            'booked':booked,
            'context':context,
            'slot':slot,
            'group':group,
            'date':date,
            'theme':theme
        }
        return render(request,"member/checkbooking.html",newcontent)
    else:
        record='Booking Seats are currently not available'
        newcontent={
            'context':context,
            'record':record
        }
        return render(request,"member/checkbooking.html",newcontent)

def confirmbooking(request):
    context=membername(request)
    if request.method=='POST':
        slot=request.POST['slot']
        date=request.POST['date']
        newcontent={
            'context':context,
            'date':date,
            'slot':slot
        }
        return render(request,"member/booking.html",newcontent)

def updatebooking(request,group):
    seat=Booking.objects.get(group=group)
    available=seat.available-1
    booked=seat.booked+1
    seat.available=available
    seat.booked=booked
    seat.save()
    return redirect('memberhome')

def seatchecking(request):
    username = request.session.get('username', 'username')
    if Application.object.filter(username=username).exists():
        message='Your seat is already booked.'
        context={
            'message':message
        }
        return render(request,"member/seatchecking.html",context)
    else:
        return redirect('memberbooking')

def bookingseat(request):
    if request.method=='POST':
        slot=request.POST['slot']
        date=request.POST['date']
        phone=request.POST['phone']
        username=request.POST['username']
        name=request.POST['name']
        group=request.POST['group']
        status='Unchecked'
        application=Application(date=date,group=group,slot=slot,username=username,phone=phone,name=name,status=status)
        application.save()
        updatebooking(request,group)
        return redirect('memberhome')

def checkpassword(request,password,confirmpassword):
    username = request.session.get('username', 'username')
    record=UserLogin.objects.get(username=username)
    databasepassword=record.password
    if(password==databasepassword):
        if(confirmpassword==databasepassword):
            messages.info(request,'Please choose new password')
            return render(request,"member/updatepassword.html")
        else:
            record.password=confirmpassword
            record.save()
            messages.info(request,'Password Updated')
            return render(request,"member/updatepassword.html")
    else:
        messages.info(request,'Password does not match')
        return render(request,"member/updatepassword.html")

def updatepassword(request):
    if request.method=='POST':
        password=request.POST['oldpassword']
        confirmpassword=request.POST['confirmpassword']
        checkpassword(request,password,confirmpassword) 
        return render(request,"member/updatepassword.html")
    else:
        return render(request,"member/updatepassword.html")

def updatedetail(request):
    username = request.session.get('username', 'username')
    if request.method=='POST':
        email=request.POST['email']
        phone=request.POST['phone']
        record=Records.object.get(username=username)
        record.email=email
        record.phone=phone
        record.save()
        messages.info(request,'Details Updated')
        return render(request,"member/updatedetail.html")

    else:
        return render(request,"member/updatedetail.html")

