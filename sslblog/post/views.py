from django.shortcuts import render,redirect,HttpResponse,get_object_or_404,reverse
from .models import Post,Comment
from django.views import generic
from django.contrib.auth.models import User
from .forms import CommentForm




# Create your views here.

def index(request):
    return render(request,"index.html")



def post(request):
    post=Post.objects.filter(status=1).order_by('created_on')
    return render(request,"post.html",{'post':post})
    

def postdetail(request,slug):
    post = get_object_or_404(Post ,slug=slug)
    comments = post.comments.all()
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request,'postdetail.html',
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form
    })








        
    



