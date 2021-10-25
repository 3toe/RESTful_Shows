from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

# GET - method should return a template that displays all the shows in a table
def index(request):
   context = {
      "Showlist" : Show.objects.all()
   }
   return render(request, "index.html", context)

# GET - method should return a template containing the form for adding a new TV show
def new(request):
   return render(request, "newshow.html")

# POST - method should add the show to the database, then redirect to /shows/<id>
def create(request):
   errors = Show.objects.validator(request.POST)
   if len(errors) > 0:
      for key, value in errors.items():
         messages.error(request, value)
      return redirect('/shows/new')
   else:
      new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], reldate=request.POST['reldate'], desc=request.POST['desc'])
      return redirect(f'/shows/{new_show.id}')

# GET - method should return a template that displays the specific show's information
def show_info(request, show_id):
   context ={
      'show' : Show.objects.get(id=show_id)
   }
   return render(request, "showinfo.html", context)

# GET - method should return a template that displays a form for editing the TV show with the id specified in the url
def show_edit(request, show_id):
   context={
      'show' : Show.objects.get(id=show_id)
   }
   return render(request, "editshow.html", context)

# POST - method should update the specific show in the database, then redirect to /shows/<id>
def show_update(request, show_id):
   errors = Show.objects.validator(request.POST)
   if len(errors) > 0:
      for key, value in errors.items():
         messages.error(request, value)
      return redirect(f'/shows/{show_id}/edit')
   else:
      show = Show.objects.get(id=show_id)
      show.title = request.POST['title']
      show.network = request.POST['network']
      show.reldate = request.POST['reldate']
      show.desc = request.POST['desc']
      show.save()
      return redirect(f'/shows/{show.id}')

# POST - method should delete the show with the specified id from the database, then redirect to /shows
def show_delete(request, show_id):
   Show.objects.get(id=show_id).delete()
   return redirect('/shows')