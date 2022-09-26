from django.shortcuts import render
from posts.models import Post, Photo
from events.models import Event


def make_list(queryset):
    my_list = []
    for q in queryset:
        my_list.append(q)
    return my_list


def home_page(request):
    posts = Post.objects.all()
    posts_list = make_list(posts)
    new_posts = [posts_list.pop(), posts_list.pop(), posts_list.pop()]
    all_events = Event.objects.all()
    events_list = make_list(all_events)
    new_events = []
    all_photos = Photo.objects.all()
    photos = []

    if all_events.count() >= 3:
        new_events = [events_list.pop(), events_list.pop(), events_list.pop()]
    elif all_events.count() == 2:
        new_events = [events_list.pop(), events_list.pop()]
    elif all_events.count() == 1:
        new_events = [events_list.pop()]

    for p in posts:
        photos.append(p.cover.url)
    for p in all_photos:
        photos.append(p.photo.url)

    context = {
        'posts': new_posts,
        'events': new_events,
        'photos': photos
    }

    return render(request, 'index.html', context=context)


def about_me(request):
    return render(request, 'about.html')


def contact_page(request):
    posts = Post.objects.all()
    all_photos = Photo.objects.all()
    photos = []

    for post in posts:
        photos.append(post.cover.url)

    for photo in all_photos:
        photos.append(photo.photo.url)

    return render(request, 'contact.html', {'photos': photos})


def gallery_page(request):
    posts = Post.objects.all()
    all_photos = Photo.objects.all()
    list_photos = []

    for post in posts:
        list_photos.append(post.cover.url)

    for photo in all_photos:
        list_photos.append(photo.photo.url)

    first_photo = list_photos[0]

    try:
        next_photos = [list_photos[1], list_photos[2], list_photos[3]]
    except IndexError:
        next_photos = None

    photos = []

    if len(list_photos) > 4:
        i = 4
        while i < len(list_photos) - 1:
            photos.append(list_photos[i])
            i += 1

    context = {
        'first_photo': first_photo,
        'next_photos': next_photos,
        'photos': photos
    }

    return render(request, 'gallery.html', context=context)
