from rest_framework import serializers
from ..models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsDetailModel
        fields = ['id','user','image','author','author_image','title','title_tags','paragraph1','paragraph2','status','type']