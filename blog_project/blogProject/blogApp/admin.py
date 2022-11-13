from django.contrib import admin
from blogApp.models import Post, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    list_filter=('status','author','publish','created') # this show the search bar at right side
    search_fields=('title','body') # this provides the search bar
    raw_id_fields=('author',)  # instate of dropdown we can select author by using id
    date_hierarchy='publish' # this provides the date & year of the post in navbar 
    ordering=['status','publish'] # this provide the orders according to our requirement of posts
    prepopulated_fields={'slug': ('title',)} # whatever i have type in title field automatically same matter written in slug field.


class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','body','created','updated','active')
    list_filter=('active','created','updated')
    search_fields=('name','email','body')


admin.site.register(Post,PostAdmin) 
admin.site.register(Comment,CommentAdmin)
# # admin.site.register(Comment)