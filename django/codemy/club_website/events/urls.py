from django.urls import path
from . import views

app_name = 'events'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name='home'),
    path('add_venue/', views.add_venue, name='add-venue'),
    path('list_venues/', views.list_venues, name='list-venues'),
    path('show_venue/<int:pk>', views.show_venue, name='show-venue'),
    path('search_venues/', views.search_venues, name='search-venues'),
    path('update_venue/<int:pk>', views.update_venue, name='update-venue'),
    path('delete_venue/<int:pk>', views.delete_venue, name='delete-venue'),
    path('write_venue_txt', views.venue_text, name='write-venue-txt'),

    path('events/', views.show_events, name='list-events'),
    path('add_event/', views.add_event, name='add-event'),
    path('update_event/<int:pk>', views.update_event, name='update-event'),
    path('delete_event/<int:pk>', views.delete_event, name='delete-event'),

]
