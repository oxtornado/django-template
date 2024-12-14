from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .models import Post, Comment
from django.contrib.auth.models import User # type: ignore

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        comment = Comment.objects.create(
            post=post,
            author=request.user,
            content=request.POST['content']
        )
        comment.save()
        return redirect('post_detail', post_id=post.id)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content, author=request.user)
        return redirect('home')
    return render(request, 'blog/add_post.html')
