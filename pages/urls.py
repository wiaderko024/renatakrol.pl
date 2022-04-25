from django.urls import path
from .views import home_page, about_me, contact_page, gallery_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('about-me/', about_me, name="about_me"),
    path('contact/', contact_page, name="contact_page"),
    path('gallery/', gallery_page, name="gallery_page"),
]
