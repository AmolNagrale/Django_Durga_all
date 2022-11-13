from os import times
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager #before running makemigrations & migrate command we have get the error, bcz to store permanant tags need to required table hence, makemigrations & migrate must be required.

# Create your models here.
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=264, unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_posts', on_delete=models.CASCADE) # author is a foreignkey pointing the data from user table on_delete=models.CASCADE that argument must be required otherwise we will get one argument missing error.
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now) # for taken current time zone
    created=models.DateTimeField(auto_now_add=True) # whenever we have updated last post on blog Application
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects=CustomManager()
    tags=TaggableManager()
    
     #as per observation created updated & published time are same                                

    class Meta:
        ordering=('-publish',) #make sure single value tuple ends with comma

    def __str__(self): # string is use to print the title anywhere in string formate
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'), self.slug])


#Model related to comment section.
class Comment(models.Model):
    post=models.ForeignKey(Post, related_name="comments",
    on_delete=models.CASCADE,)
    name=models.CharField(max_length=32)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    class Meta:
        ordering=('-created',)
    def __str__(self):
        return 'commented By {} on  {}'.format(self.name, self.post)
    