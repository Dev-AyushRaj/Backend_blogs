from django.contrib import admin
from .models import Blog
#register your models here
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','tittle','author_name','created_at']
    search_fields = ["tittle",'author_name']
    list_filter = ['created_at',]