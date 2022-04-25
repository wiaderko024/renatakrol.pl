from django.urls import path
from .views import pricing_page


app_name = 'pricing'


urlpatterns = [
    path('', pricing_page, name="pricing_page"),
]
