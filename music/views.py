from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import View
from .models import Album
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class ALbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title','gener', 'album_logo']


class ALbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title','gener', 'album_logo']


class ALbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index.html')


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/reg_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def podt(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            passward = form.cleaned_data['password']
            user.set_password(passward)
            user.save()





