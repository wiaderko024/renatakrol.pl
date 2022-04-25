from django.urls import path
from .views import all_events_page, event_page


app_name = 'events'


urlpatterns = [
    path('', all_events_page, name="all_events_page"),
    path('<int:id>/', event_page, name="event_page"),
]
