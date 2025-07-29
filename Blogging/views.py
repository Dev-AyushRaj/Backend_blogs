from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer

# Create your views here.
class BloglistAPIView(APIView):
    
    def get(self,request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many= True)
        return Response(serializer.data)