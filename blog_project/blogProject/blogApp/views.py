from django.core.checks import messages
from django.shortcuts import get_object_or_404, render
from blogApp.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from taggit.models import Tag
from blogApp.forms import CommentForm

# Create your views here.

# this is the fuction based view of listview

def post_list_view(request, tag_slug=None):
    post_list=Post.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag, slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])

    paginator= Paginator(post_list,3)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)

    return render (request,'blogApp/post_list.html',{'post_list':post_list, 'tag':tag})

# this is the class based view code for listview
from django.views.generic import ListView
class PostListView(ListView):
    model=Post
    paginate_by=2

def post_detail_view(request, year, month, day, post):
    post= get_object_or_404(Post, slug=post,
                                    status='published', 
                                    publish__year=year, 
                                    publish__month=month,
                                    publish__day=day)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True

    else:
        form=CommentForm()
    return render(request,'blogApp/post_detail.html',{'post':post, 'form':form, 'csubmit':csubmit, 'comments':comments})


from django.core.mail import send_mail
from blogApp.forms import EmailSendForm

def mail_send_view(request,id):
    post=get_object_or_404(Post, id=id, status='published')
    sent=False # when we have to post request  
    if request.method=='POST':
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            post_url=request.build_absolute_uri(post.get_absolute_url())
            subject='{}({}) recommends you to read"{}"'.format(cd['name'],cd['email'], post.title)
            message='Read Post At:\n {}\n\n\'s Comments:\n{}'.format(post_url,cd['name'],cd['comments'])
            send_mail(subject,message,'amol.practice.test@gmail.com',[cd['to']])
            sent=True # when we have to get request to the data 
    else:
        form=EmailSendForm()
    return render(request,'blogApp/sharebymail.html',{'form':form,'post':post, 'sent':sent})
    
