from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from films.forms import RegisterForm
from films.models import Film, Song
from django.views.generic.list import ListView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    
class Login(LoginView):
    template_name = 'registration/login.html'

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)


class FilmList(ListView):
    template_name = 'films.html'
    model = Film
    context_object_name = 'films'

    def get_queryset(self):
        user = self.request.user
        return user.films.all()

class SongList(ListView):
    template_name = 'songs.html'
    model = Song
    context_object_name = 'songs'

    def get_Queryset(self):
        user = self.request.user
        return user.songs.all()


def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div id='username-error' class='error'>This username already exists</div>")
    else:
        return HttpResponse("<div id='username-error' class='success'>This username is available</div>")

def add_film(request):
    name = request.POST.get('filmname')

    # add film
    film = Film.objects.create(name=name)
    
    # add the film to the user's list
    request.user.films.add(film)

    # return template fragment with all the user's films
    return render(request, 'partials/film_item.html', {'film': film})

def add_song(request):
    name = request.POST.get('songname')
    # add songs
    song = Song.objects.create(name=name)
    request.user.songs.add(song)
    songs = request.user.songs.all()
    return render(request, 'partials/song-list.html', {'songs':songs})


def delete_film(request, pk):
    # print(pk)
    # print(type(pk))
    # remove the film from the user's list
    # film = Film.objects.get(id=pk)
    # film = Film.objects.get(id=pk)
    # request.user.films.remove(film)

    data = request.user.films.get(id=pk)
    data.delete()
    # return template fragment with all the user's films
    films = request.user.films.all()
    return JsonResponse('film removed',safe=False)