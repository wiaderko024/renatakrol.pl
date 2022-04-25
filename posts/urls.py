from django.urls import path
from .views import all_posts_page, post_page


app_name = 'posts'


urlpatterns = [
    path('', all_posts_page, name="all_posts_page"),
    path('<int:id>/', post_page, name="post_page"),
]
