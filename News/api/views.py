from ..models import *
from .serializers  import UserSerializer, NewsDetailSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,DestroyModelMixin,ListModelMixin, RetrieveModelMixin
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class NewsViewApi(GenericAPIView, ListModelMixin,CreateModelMixin):
    queryset = NewsDetailModel.objects.all()
    serializer_class = NewsDetailSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['^author','title']
    ordering_fields = ['author', 'status']

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
class NewsDetailViewSet(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
    queryset = NewsDetailModel.objects.all()
    serializer_class = NewsDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)