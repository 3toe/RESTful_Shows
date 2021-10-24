from django.urls import path     
from . import views

urlpatterns = [
   # GET - method should return a template that displays all the shows in a table
   path('shows', views.index),
   # GET - method should return a template containing the form for adding a new TV show
   path('shows/new', views.new),
   # POST - method should add the show to the database, then redirect to /shows/<id>
   path('shows/create', views.create),
   # GET - method should return a template that displays the specific show's information
   path('shows/<int:show_id>', views.show_info),
   # GET - method should return a template that displays a form for editing the TV show with the id specified in the url
   path('shows/<int:show_id>/edit', views.show_edit),
   # POST - method should update the specific show in the database, then redirect to /shows/<id>
   path('shows/<int:show_id>/update', views.show_update),
   # POST - method should delete the show with the specified id from the database, then redirect to /shows
   path('shows/<int:show_id>/destroy', views.show_delete)   
]