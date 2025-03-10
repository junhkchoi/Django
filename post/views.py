from django.shortcuts import render,redirect

from . models import Post

# 공지사항 목록
def post_list(request):
    return render(request, 'post/post_list.html')

# CRUD
def detail_post(request):
    return render(request, 'post/detail_post.html')

def create_post(request):
    if request.method == 'POST':
        post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('post_list')
    return render(request, 'post/create_post.html')

def update_post(request):
    return render(request, 'post/update_post.html')

def delete_post(request):
    return render(request, 'post/delete_post.html')