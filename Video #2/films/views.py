from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth import get_user_model
from . models import Film
from django.views.generic.list import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from films.forms import RegisterForm

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

    def get_Queryset(self):
        films = self.request.user.films.all()
        print(films)
        return films


def filmlist(request):
    films = Film.objects.all()
    p = Paginator(films,5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    return render(request, 'base.html', context)


def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div id='username-error' class='error'>This username already exists</div>")
    else:
        return HttpResponse("<div id='username-error' class='success'>This username is available</div>")

    
def add_film(request):
    name = request.POST.get('filmname')
    film = Film.objects.create(name=name)
    #add the films to the user's film
    request.user.films.add(film)
    #return templates with all of the user's films
    films = request.user.films.all()
    return render(request, 'partials/film-list.html', {'films':films})

def delete_film(request, pk):
    #remove theuser films from user's list
    film = Film.objects.get(id=pk)
    film.delete()
    # film = film.users.remove(request.user)
    # print(film)
    #return template fragment
    # print(request.user)
    films = request.user.films.all()
    return render(request, 'partials/film-list.html', {'films':films})
    