from django.contrib.auth.models import User,auth,Group
from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.db.models import Sum,Count
from .models import StaffRecords,Records,Content,Booking
from member.models import Application,Contactus
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.views.generic import ListView, DetailView 
#from .forms import ImageUploadForm
from django.core.files.storage import FileSystemStorage
# Create your views here.

def staffname(request):
    request.session['username']=request.user.username
    username=request.session['username']
    ab=StaffRecords.object.get(username=username)
    name=ab.name
    image=ab.image
    context={
        'name':name,
        'image':image
    }
    return context

def login(request):
    return render(request,"staff/page-login.html")

def homepage(request):
    context=staffname(request)
    arts_count=Records.object.filter(Q(group='Arts')).count()
    singing_count=Records.object.filter(Q(group='Singing')).count()
    dancing_count=Records.object.filter(Q(group='Dancing')).count()
    pd_count=Records.object.filter(Q(group='Personality Development')).count()
    arts_sum=Records.object.filter(Q(group='Arts')).aggregate(a=Sum('fees'))
    singing_sum=Records.object.filter(Q(group='Singing')).aggregate(b=Sum('fees'))
    dancing_sum=Records.object.filter(Q(group='Dancing')).aggregate(c=Sum('fees'))
    pd_sum=Records.object.filter(Q(group='Personality Development')).aggregate(d=Sum('fees'))
    as_count=Records.object.filter(Q(group='Singing'),Q(month='April')).count()
    ms_count=Records.object.filter(Q(group='Singing'),Q(month='May')).count()
    ad_count=Records.object.filter(Q(group='Dancing'),Q(month='April')).count()
    md_count=Records.object.filter(Q(group='Dancing'),Q(month='May')).count()
    aa_count=Records.object.filter(Q(group='Arts'),Q(month='April')).count()
    ma_count=Records.object.filter(Q(group='Arts'),Q(month='May')).count()
    apd_count=Records.object.filter(Q(group='Personality Development'),Q(month='April')).count()
    mpd_count=Records.object.filter(Q(group='Personality Development'),Q(month='May')).count()
    as_sum=Records.object.filter(Q(group='Singing'),Q(month='April')).aggregate(aa=Sum('fees'))
    ms_sum=Records.object.filter(Q(group='Singing'),Q(month='May')).aggregate(bb=Sum('fees'))
    ad_sum=Records.object.filter(Q(group='Dancing'),Q(month='April')).aggregate(cc=Sum('fees'))
    md_sum=Records.object.filter(Q(group='Dancing'),Q(month='May')).aggregate(dd=Sum('fees'))
    aa_sum=Records.object.filter(Q(group='Arts'),Q(month='April')).aggregate(ee=Sum('fees'))
    ma_sum=Records.object.filter(Q(group='Arts'),Q(month='May')).aggregate(ff=Sum('fees'))
    apd_sum=Records.object.filter(Q(group='Personality Development'),Q(month='April')).aggregate(gg=Sum('fees'))
    mpd_sum=Records.object.filter(Q(group='Personality Development'),Q(month='May')).aggregate(hh=Sum('fees'))
    artsum=arts_sum.pop('a')
    dancesum=dancing_sum.pop('c')
    singsum=singing_sum.pop('b')
    pdsum=pd_sum.pop('d')
    as_sum=as_sum.pop('aa')
    ms_sum=ms_sum.pop('bb')
    ad_sum=ad_sum.pop('cc')
    md_sum=md_sum.pop('dd')
    aa_sum=aa_sum.pop('ee')
    ma_sum=ma_sum.pop('ff')
    apd_sum=apd_sum.pop('gg')
    mpd_sum=mpd_sum.pop('hh')
    
    default=' '
    a=0
    
    newcontent={
        'context':context,
        'default':default,
        'a':a,
        'ac':arts_count,
        'dc':dancing_count,
        'sc':singing_count,
        'pdc':pd_count,
        'as':artsum,
        'ds':dancesum,
        'ss':singsum,
        'pds':pdsum,
        'ab':as_count,
        'bc':ms_count,
        'cd':ad_count,
        'de':md_count,
        'ef':aa_count,
        'fg':ma_count,
        'gh':apd_count,
        'hi':mpd_count,
        'xa':as_sum,
        'xb':ms_sum,
        'xc':ad_sum,
        'xd':md_sum,
        'xe':aa_sum,
        'xf':ma_sum,
        'xg':apd_sum,
        'xh':mpd_sum,
    }
    return render(request,"staff/index.html",newcontent)

def addcontent(request):
    context=staffname(request)
    return render(request,"staff/addcontent.html",context)

def addrecord(request):
    context=staffname(request)
    return render(request,"staff/addrecord.html",context)

def booking(request):
    context=staffname(request)
    return render(request,"staff/booking.html",context)

def deletebooking(request):
    context=staffname(request)
    return render(request,"staff/deletebooking.html",context)


def seatbooking(request):
    if request.method == 'POST':
        theme=request.POST["theme"]
        available=request.POST["available"]
        date=request.POST["date"]
        booked=request.POST["booked"]
        group=request.POST["group"]
        slot=request.POST["slot"]
        if Booking.object.filter(Q(group=group),Q(slot=slot),Q(date=date)).exists():
            messages.info(request,'Record already exists')
            return render(request,"staff/booking.html")

        else:
            
            booking=Booking(date=date,group=group,slot=slot,available=available,booked=booked,theme=theme)
            booking.save()
            context=staffname(request)
            messages.info(request,'Record successfully Added')
            return render(request,"staff/booking.html",context)

def applicationview(request):
    applications=Application.objects.all()
    context=staffname(request)
    newcontent={
        'content':context,
        'applications':applications,   
    }
    return render(request,"staff/applicationview.html",newcontent)

def contentview(request):
    contents=Content.objects.all()
    context=staffname(request)
    newcontent={
        'content':context,
        'contents':contents,
    }
    return render(request,"staff/contentview.html",newcontent)

def recordview(request):
    records=Records.objects.all()
    context=staffname(request)
    paginator = Paginator(records,5)
    page = request.GET.get('page')
    users = paginator.get_page(page)
    newcontent={
        'content':context,
        'records':records,
        'users':users,
        'page':page
    }
    return render(request,"staff/recordview.html",newcontent)


def forget(request):
    return render(request,"staff/pages-forget.html")

def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('homepage')

        else:
            messages.info(request,'Invalid user credentials')
            return redirect('login')

    else:
        return render(request,'staff/page-login.html')

def logout(request):
    return render(request,'staff/page-login.html')

def recordaddition(request):
    
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        name=request.POST['name']
        phone=request.POST["phone"]
        email=request.POST["email"]
        date=request.POST["date"]
        status=request.POST["status"]
        group=request.POST["group"]
        slot=request.POST["slot"]
        fees=request.POST["fees"]
        address=request.POST["address"]
        if Records.object.filter(username=username).exists():
            username=showvalidation(request,username)
            return username

        else:
            month=dateconvert(request,date)
            record=Records(username=username,password=password,name=name,phone=phone,email=email,date=date,
            status=status,group=group,slot=slot,fees=fees,address=address,month=month)
            record.save()
            messages.info(request,'Member successfully Added')
            return render(request,"staff/addrecord.html")

def showvalidation(request,username):
    context={
        'one':'username already exist in records'
    }
    messages.info(request,'Record is not submitted')
    return render(request,"staff/addrecord.html",context)

def contentaddition(request):
    
    if request.method == 'POST':
        article=request.POST['article']
        heading=request.POST['heading']
        date=request.POST['date']
        group=request.POST["group"]
        desc=request.POST["desc"]
        
        if Content.objects.filter(Q(article=article),Q(group=group)).exists():
            article=validate(request,article)
            return article

        else:
            content=Content(article=article,heading=heading,date=date,group=group,desc=desc)
            content.save()
            messages.info(request,'Content successfully Added')
            return render(request,"staff/addcontent.html")

def validate(request,article):
    context={
        'one':'Article already exist in Content '
    }
    messages.info(request,'Duplicate Content is not Allowed')
    return render(request,"staff/addcontent.html",context)

def applicationupdate(request,pk):
    record=Application.object.get(pk=pk)
    
    slot=record.slot
    username=record.username
    status=record.status
    context={
        
        'slot':slot,
        'status':status, 
        'username':username   
    }
    return render(request,"staff/applicationupdate.html",context)

def updateapplication(request):
   if request.method == "POST":
        status=request.POST['status']
        username=request.POST['username']
        ab=Application.objects.get(username=username)
        ab.status=status
        ab.save()
        messages.info(request,'Application Status Updated')
        return render(request, "staff/applicationupdate.html") 

def contentupdate(request,pk):
    record=Content.object.get(pk=pk)
    heading=record.heading
    desc=record.desc
    article=record.article
    group=record.group
    context={
        'heading':heading,
        'desc':desc,
        'article':article, 
        'group':group   
    }
    return render(request,"staff/contentupdate.html",context)

def updatecontent(request):
   if request.method == "POST":
        heading=request.POST['heading']
        desc=request.POST['desc']
        article=request.POST['article']
        group=request.POST['group']
        
        ab=Content.objects.get(Q(article=article),Q(group=group))
        ab.heading=heading
        ab.desc=desc
        ab.save()
        messages.info(request,'Content Updated')
        return render(request, "staff/contentupdate.html")

def recordupdate(request,pk):
    record=Records.object.get(pk=pk)
    username=record.username
    name=record.name
    email=record.email
    phone=record.phone
    slot=record.slot
    address=record.address
    status=record.status
    context={
        'username':username,
        'name':name,
        'phone':phone,
        'email':email,
        'address':address,
        'status':status,
        'slot':slot  
    }
    return render(request,"staff/recordupdate.html",context)

def updaterecord(request):
   if request.method == "POST":
        username=request.POST['username']
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        address=request.POST['address']
        status=request.POST['status']
        slot=request.POST['slot']
        
        ab=Records.object.get(username=username)
        ab.status=status
        ab.address=address
        ab.name=name
        ab.slot=slot
        ab.email=email
        ab.phone=phone
        ab.save()
        messages.info(request,'Record Updated')
        return render(request, "staff/recordupdate.html") 
 
class RecordListView(ListView):
    model=Records
    context_object_name = 'records'
    ordering = ['username']
    paginate_by = 5
    template_name='staff/recordview.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        username=self.request.session['username']
        ab=StaffRecords.object.get(username=username)
        data['name'] = ab.name
        data['image']=ab.image
        return data

class ContactListView(ListView):
    model=Contactus
    context_object_name = 'records'
    paginate_by = 5
    template_name='staff/contactus.html'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        username=self.request.session['username']
        ab=StaffRecords.object.get(username=username)
        data['name'] = ab.name
        data['image']=ab.image
        return data

class ContentListView(ListView):
    model=Content
    context_object_name = 'records'
    paginate_by = 5
    template_name='staff/contentview.html'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        username=self.request.session['username']
        ab=StaffRecords.object.get(username=username)
        data['name'] = ab.name
        data['image']=ab.image
        return data
    

class ApplicationListView(ListView):
    model=Application
    context_object_name = 'records'
    paginate_by = 5
    template_name='staff/applicationview.html'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        username=self.request.session['username']
        ab=StaffRecords.object.get(username=username)
        data['name'] = ab.name
        data['image']=ab.image
        return data

class BookingListView(ListView):
    model=Booking
    context_object_name = 'records'
    paginate_by = 5
    template_name='staff/deletebooking.html'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        username=self.request.session['username']
        ab=StaffRecords.object.get(username=username)
        data['name'] = ab.name
        data['image']=ab.image
        return data

def bookingdelete(request,pk):
    booking=Booking.object.get(pk=pk)
    booking.delete()
    return redirect('deletebooking')

def bookingview(request):
    context=staffname(request)
    return render(request,"staff/bookinglist.html",context)

def bookinglist(request):
    if request.method == 'POST':
        date=request.POST["date"]
        group=request.POST["group"]
        slot=request.POST["slot"]
        records=Application.object.filter(Q(group=group),Q(slot=slot),Q(date=date))

        context={
            'records':records,
            'group':group,
            'slot':slot,
            'date':date
        }
        return render(request,"staff/bookingview.html",context)

def dateconvert(request,date):
    month=date[0:2]
    if(month=='01'):
        a='January'
    elif(month=='02'):
        a='Febuary'
    elif(month=='03'):
        a='March'
    elif(month=='04'):
        a='April'
    elif(month=='05'):
        a='May'
    elif(month=='06'):
        a='June'
    elif(month=='07'):
        a='July'
    elif(month=='08'):
        a='August'
    elif(month=='09'):
        a='September'
    elif(month=='10'):
        a='October'
    elif(month=='11'):
        a='November'
    else:
        a='December'
    return a

   