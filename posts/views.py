from django.shortcuts import render
from .models import Post, Photo


def all_posts_page(request):
    posts = reversed(Post.objects.all())
    return render(request, 'posts.html', {'posts': posts})


def post_page(request, id):
    post = Post.objects.get(pk=id)
    all_photos = Photo.objects.filter(post=post.id)
    first_photos = []
    photos = []

    i = 0
    for photo in all_photos:
        if i < 3:
            first_photos.append(photo)
        else:
            photos.append(photo)

        i += 1

    context = {
        'post': post,
        'first_photos': first_photos,
        'photos': photos
    }

    return render(request, 'post.html', context=context)
