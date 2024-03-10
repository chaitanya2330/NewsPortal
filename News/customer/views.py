# from django.shortcuts import render, get_object_or_404,redirect, HttpResponse
# from django.contrib.auth.decorators import login_required
# from .forms import BasicUserForm,BasicCustomerForm, NewsDetailForm,ProfileUpdateForm,UserUpdateForm
# from django.urls import reverse
# from ..models import CustomerProfileModel
# from ..models import *
# from django.contrib import messages
# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth import update_session_auth_hash
#
# # @login_required()
# # def AuthorProfile(request):
# #     return redirect(reverse('customer:profile'))
# @login_required
# def AuthorProfile(request):
#     currentuser = CustomerProfileModel.objects.get(id=request.user.id)
#     user_form = BasicUserForm(instance=request.user)
#     customer_form = BasicCustomerForm(instance=currentuser)
#     password_form = PasswordChangeForm(request.user, request.POST)
#     if request.method == 'POST':
#         if request.POST.get('action') == 'update_profile':
#             user_form = BasicUserForm(request.POST, instance=request.user)
#             customer_form = BasicCustomerForm(request.POST,request.FILES, instance=currentuser)
#             if user_form.is_valid() and customer_form.is_valid():
#                 user_form.save()
#                 customer_form.save()
#                 print(customer_form)
#                 return redirect(reverse('customer:profile'))
#             elif request.POST.get('action') == 'update_password':
#                 if password_form.is_valid():
#                     user = password_form.save()
#                     update_session_auth_hash(request, user)
#                     messages.success(request, "Your password has been updated")
#                     return redirect(reverse('customer:profile'))
#
#     # currentuser = CustomerProfileModel.objects.filter(user=request.user.id).first()
#     # user_form = BasicUserForm(request.POST, instance=request.user)
#     # customer_form = BasicCustomerForm(request.POST,request.FILES,instance=currentuser)
#     # if request.method == 'POST':
#     #     if request.POST.get('action') == 'update_profile':
#     #         if user_form.is_valid() and customer_form.is_valid():
#     #             user_form.save()
#     #             customer_form.save()
#     #             messages.success(request,"Your Profile has been updated")
#     #     elif request.POST.get('action') == 'update_password':
#     #         if password_form.is_valid():
#     #             user = password_form.save()
#     #             update_session_auth_hash(request,user)
#     #             messages.success(request,"Your password has been updated")
#     #             return redirect(reverse('customer:profile'))
#
#     return render(request,"customer/profile.html",{
#         "user_form":user_form,
#         "customer_form":customer_form,
#         "currentuser":currentuser,
#         "password_form":password_form,
#
#     })
#
# from django.contrib.auth import get_user_model
# # @login_required
# # def profile(request):
# #     currentuser = CustomerProfileModel.objects.get(id=request.user.id)
# #     if request.method == 'POST':
# #
# #         u_form=UserUpdateForm(request.POST, instance=request.user)
# #         p_form=ProfileUpdateForm(request.POST, request.FILES, instance=currentuser)
# #
# #         if u_form.is_valid() and p_form.is_valid():
# #             u_form.save()
# #             p_form.save()
# #             return redirect('customer/profiles')
# #     else:
# #         u_form=UserUpdateForm(instance=request.user)
# #         p_form=ProfileUpdateForm(instance=currentuser)
# #     context = {
# #         'u_form':u_form,
# #         'p_form':p_form,
# #     }
# #     return render(request,'customer/profiles.html')
# @login_required
# def AuthorProfilePOST(request):
#     currentuser = NewsDetailModel.objects.filter(author=request.user).first()
#
#     if request.method == 'POST':
#         News_form = NewsDetailForm(request.POST, request.FILES, instance=currentuser)
#         if News_form.is_valid():
#             News_form.save()
#     else:
#         News_form = NewsDetailForm(instance=currentuser)
#
#     return render(request,"customer/profile_post.html",{
#         "News_form":News_form,
#         "currentuser":currentuser,
#     })
#
# @login_required(login_url="/login/?next=/customer/")
# def Test(request):
#
#     return render(request,"customer/test.html",{
#     })
