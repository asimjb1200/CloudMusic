from django.views import generic
from .models import Album
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.views.generic import View
from .forms import UserForm

class IndexView(generic.ListView): # used ListView because the index page will be a list of all the albums
    # specify the template that will be used
    template_name = 'music/index.html'
    # query the database for the data that you want, and then return it to the template for user viewing
    context_object_name = 'all_albums'

    def get_queryset(self):
        # return "object_list" object_list is the default variable name
        return Album.objects.all() # we want all of the albums for the index page in a list of objects.

class DetailsView(generic.DetailView):# used detail view because this page is for details about a specific album
    # specify the model you want the details of
    model = Album
    # specify the template you want to plug the model into
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):# when we want to create a new album object
    # what model am I using for the object?
    model = Album
    # what fields do I need in this form for the user to fill out upon creation
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')
    
class UserFormView(View):
    # what is the form's blueprint/class?
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # whenever the user calls the form it's a get request, go here and display a blank form
    def get(self, request):
        form = self.form_class(None)# no data by default in the blank form
        return render(request, self.template_name, {'form': form})
    
    # process form data
    def post(self, request):
        form = self.form_class(request.POST) # pass in the user's data to that was submitted in form 

        if form.is_valid():
            user = form.save(commit=False) # create an object from the form, but don't save the form's data to the database yet

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()# now save them to the database

            # returns User onjects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    # request.user.username
                    # now redirect them to a page after login
                    return redirect('music:index')
                    
        # if it doesn't work, have them try again
        return render(request, self.template_name, {'form': form})
        






