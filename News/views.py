from django.shortcuts import render, get_object_or_404,redirect, HttpResponse
from .models import ContactPageModel,NewsDetailModel
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator
from django.urls import reverse
from .forms import *

# Create your views here.

def HomePageView(request):
    news = NewsDetailModel.objects.all()
    latest_news = NewsDetailModel.objects.filter(status='Latest')[:2]
    latest_news_reverseorder = NewsDetailModel.objects.filter(status='Latest')[2:4]
    popular_news = NewsDetailModel.objects.filter(status='Popular')[:3]
    carsonal_filter = NewsDetailModel.objects.all()[:3]
    carsonal_filter_box = NewsDetailModel.objects.all()[3:7]
    flicker_photo = NewsDetailModel.objects.all()[:6]
    context = {
        'news': news,
        'related':latest_news,
        'popular_news':popular_news,
        'reverse_latest':latest_news_reverseorder,
        'carsonal_filter':carsonal_filter,
        'carsonal_filter_box':carsonal_filter_box,
        'breaking_news':news,
        'flicker_photo':flicker_photo,
    }
    return render(request, 'News/home.html', context)

def DetailPageView(request,id):
    object = get_object_or_404(NewsDetailModel,pk=id)
    related_news = NewsDetailModel.objects.filter(status=object.status).exclude(id=id)[:3]
    reviewsdetails = Review.objects.all()
    flicker_photo = NewsDetailModel.objects.all()[:6]
    popular_news = NewsDetailModel.objects.filter(status='Popular')[:3]
    context = {
        'object': object,
        'related':related_news,
        'reviewsdetails':reviewsdetails,
        'flicker_photo': flicker_photo,
        'popular_news':popular_news,

    }
    return render(request, 'News/NewsDetail.html', context)

def SearchBarView(request):
    """
        This is only used searchbar
    :param request:
    :return:
    """
    if request.method == "GET":
        search = request.GET.get('q')
        post = NewsDetailModel.objects.filter(title__icontains= search)
        flicker_photo = NewsDetailModel.objects.all()[:6]
        popular_news = NewsDetailModel.objects.filter(status='Popular')[:3]
        return render(request,'News/searchbar.html',{
            'post':post,
            'flicker_photo':flicker_photo,
            'popular_news':popular_news,
        })

def ContactPageView(request):
    if request.method == 'POST':
        forms = ContactForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Data inserted successfully")
            return redirect('contact')
        else:
            messages.warning(request, "Data was not inserted")
    else:
        forms = ContactForm()
    flicker_photo = NewsDetailModel.objects.all()[:6]
    popular_news = NewsDetailModel.objects.filter(status='Popular')[:3]
    context = {
        'forms':forms,
        'flicker_photo':flicker_photo,
        'popular_news':popular_news,
    }
    return render(request, 'News/contact.html', context)

def HealthPageView(request):
    objects = NewsDetailModel.objects.filter(type='Heath')
    popular_news = NewsDetailModel.objects.filter(status='Popular')[:3]
    flicker_photo = NewsDetailModel.objects.all()[:6]
    return render(request,'News/health.html',{
        'objects':objects,
        'popular_news':popular_news,
        'flicker_photo':flicker_photo,
    })

def TechnologyPageView(request):
    objects = NewsDetailModel.objects.filter(type='Technlogy')
    popular_news = NewsDetailModel.objects.filter(status='Popular')[:3]
    flicker_photo = NewsDetailModel.objects.all()[:6]
    return render(request,'News/health.html',{
        'objects':objects,
        'popular_news':popular_news,
        'flicker_photo':flicker_photo,
    })
def RegistrationView(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "username already exits! Please try some other username")
            return redirect('register')

        if User.objects.filter(email=email):
            messages.error(request, "Email already register Please try some other email")

        if len(username) > 10:
            messages.error(request, "Username must be in 10 characters")

        if pass1 != pass2:
            return HttpResponse("Password didn't match!")

        if not username.isalnum():
            messages.error(request, "Username must be in letters and numbers")

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        
        messages.success(request,"Your successfully created")
        return redirect('login')
    return render(request,'Authentication/register.html')

def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request,user)
            return redirect("profile/")

        # elif request.user.pass1 != pass1:
        #     return redirect("")
        else:
            messages.error(request,"Bad credential")
            return redirect('/')
    flicker_photo = NewsDetailModel.objects.all()[:6]
    popular_news = NewsDetailModel.objects.filter(status='Popular')[:3]

    return render(request,'Authentication/login.html',{
        'flicker_photo':flicker_photo,
        'popular_news':popular_news,
         })

def LogoutView(request):
    logout(request)
    messages.success(request,"You successfully logout.")
    return redirect('/')

from .forms import *
def Submit_ReviewView(request, id):
    """
        Submit the review rating in database and display the rating and review in frontend side.

    """
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = Review.objects.get(user__id=request.user.id,news__id= id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request,"Thank you! Your review updated")
            return redirect(url)
        except Review.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = Review()
                data.subject = form.cleaned_data['subject']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.news_id = id
                data.user_id = request.user.id
                data.save()
                messages.success(request, "Thank you! Your review has been submited")
                return redirect(url)

def Update_User(request):
    return render(request,"Update_User.html")

@login_required
def AuthorProfile(request):
    currentuser = CustomerProfileModel.objects.get(id=request.user.id)
    user_form = BasicUserForm(instance=request.user)
    customer_form = BasicCustomerForm(instance=currentuser)
    password_form = PasswordChangeForm(request.user, request.POST)
    flicker_photo = NewsDetailModel.objects.all()[:6]
    News_form = NewsDetailForm(request.POST, request.FILES)
    popular_news = NewsDetailModel.objects.filter(status='Popular')[:3]

    if request.method == 'POST':
        if request.POST.get('action') == 'update_profile':
            user_form = BasicUserForm(request.POST, instance=request.user)
            customer_form = BasicCustomerForm(request.POST,request.FILES, instance=currentuser)
            if user_form.is_valid() and customer_form.is_valid():
                user_form.save()
                customer_form.save()
                return redirect("/")
        elif request.POST.get('action') == 'update_password':
            if password_form.is_valid():
                    user = password_form.save()
                    update_session_auth_hash(request, user)
                    messages.success(request, "Your password has been updated")

        elif request.POST.get('action') == 'add_news':
            if News_form.is_valid():
                    News_form.save()
                    messages.success(request, "Congratulations your post successfully submitted.")



    return render(request,'News/test.html',{
        "user_form":user_form,
        "customer_form":customer_form,
        "currentuser":currentuser,
        "password_form":password_form,
        "News_form": News_form,
        "flicker_photo":flicker_photo,
        "popular_news":popular_news,
    })


