from django.shortcuts import render
from .models import Post
from .serializers import PostSerializers

# classed_based Views

from django.http import Http404

from rest_framework import generics
from rest_framework import mixins

# Create your views here.

class genericAPIView(generics.GenericAPIView, 
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = PostSerializers
    queryset = Post.objects.all()
    lookup_field = 'id'

    def get(self, request, id):
        if id:
            return self.retrieve(request)
        else:
          return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
    def put(self, request, id = None):
        return self.update(request)
    
    def delete(self, request, id = None):
        return self.destroy(request)
