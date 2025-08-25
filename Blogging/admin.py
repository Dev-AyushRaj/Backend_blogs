from django.contrib import admin
from .models import Blog
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'tittle', 'author_name', 'created_at')  # show these columns in admin list
    search_fields = ('tittle', 'author_name')  # add search bar
    list_filter = ('created_at',)  # filter option in side bar