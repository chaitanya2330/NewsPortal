from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.

choice = (
    ('Featured', 'Featured'),
    ('Popular', 'Popular'),
    ('Latest', 'Latest')
)
news_type = (
    ('Heath', 'Heath'),
    ('Technlogy', 'Technlogy'),
    ('Other', 'Other')
)
from django.contrib.auth.models import User
class NewsHomeModel(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=150)
    status = models.CharField(choices=choice, max_length=100)
class NewsDetailModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True,upload_to="img/")
    author = models.CharField(max_length=150)
    author_image = models.ImageField(null=True, upload_to="img/")
    title = models.CharField(max_length=150)
    title_tags = models.CharField(max_length=100)
    paragraph1 = models.TextField(max_length=5000)
    paragraph2 = models.TextField(max_length=5000, null=True)
    status = models.CharField(choices=choice,max_length=100)
    created_at = models.DateTimeField(auto_now_add=timezone.now())
    type = models.CharField(choices=news_type, max_length=100, null=True)

    def __str__(self):
        return self.author


class CustomerProfileModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to='customer/avatars/',blank=True, null=True)

def customer_name_startwith_a(value):
    if not value.startswith('a'):
        raise ValidationError('The word start with a')

def length_email(value):
    if len(value) < 10:
        raise ValidationError('Length of name would be more than 4')

class ContactPageModel(models.Model):
    name = models.CharField(max_length=100, validators=[customer_name_startwith_a])
    email = models.EmailField(max_length=250, validators=[length_email])
    subject = models.CharField(max_length=300)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    news = models.ForeignKey(NewsDetailModel, on_delete=models.CASCADE, null=True)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=300,blank=True)
    review = models.TextField(max_length=1000,blank=True)
    status = models.BooleanField(default=True,null=True)
    created_at = models.DateTimeField(auto_now_add=timezone.now(),null=True)
    updated_date = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.subject