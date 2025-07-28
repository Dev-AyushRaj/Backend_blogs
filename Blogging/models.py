from django.db import models

# Create your models here.
class Blog(models.Model):
    tittle = models.CharField(max_length=255)
    categorie = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    author_email = models.EmailField(unique=True)
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    blog_intro = models.TextField()
    content = models.TextField()
    

class Blog_tag(models.Model):
    tag_name = models.CharField(max_length=255)
    blog = models.ManyToManyField(Blog, related_name= "tags")