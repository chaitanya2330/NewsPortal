
from django.urls import path, include
from .views import *
from .customer import views as customerviews


customer_urlpatterns = [
    # path('profile/',customerviews.AuthorProfile,name='profile'),
    # path('profile_post/',customerviews.AuthorProfilePOST,name='profile_post'),
    # path('profile_posts/',customerviews.profile,name='profile_posts'),
    # path('test1/',customerviews.Test,name='test1'),
]
urlpatterns = [
    path('',HomePageView,name= 'home'),
    path('<int:id>/',DetailPageView,name= 'news_detail'),
    path('searchbar/',SearchBarView,name='searchbar'),
    path('login/profile/',AuthorProfile,name='profile'),
    path('login/',LoginView,name='login'),
    path('logout/',LogoutView,name='logout'),
    path('register/',RegistrationView,name='register'),
    path('contact/', ContactPageView, name='contact'),
    path('health/', HealthPageView, name='health'),
    path('technology/', TechnologyPageView, name='technology'),
    path('submit_review/<int:id>/',Submit_ReviewView,name='submit_review'),


    path('update_user/',Update_User,name='update_user'),
    path('customer/',include((customer_urlpatterns,'customer'))),

]