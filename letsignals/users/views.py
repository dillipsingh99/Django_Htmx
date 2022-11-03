from django.shortcuts import render, redirect, get_object_or_404
from . models import Profile
from . forms import ProfileForm
from django.http import HttpResponse

def listProfile(request):
    data = Profile.objects.all()
    return render(request, 'listProfile.html', {'data':data})


def createProfile(request):
    form = ProfileForm()
    if request.method=="POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            data = form.save()
            return render(request, 'listProfile.html', {'data':data})
    
    return render(request, 'createProfile.html', {'form':form})

def editProfile(request, pk):
    data = get_object_or_404(Profile, pk=pk)   
    if request.method=='POST':
        form = ProfileForm(request.POST, instance=data)
        data = form.save()
        return redirect('listProfile')
    else:
        form = ProfileForm(instance = data)
    return render(request, 'createProfile.html', {
        'form':form,
        'data':data,
    }) 


def setcookie(request):
    html = HttpResponse("<h1>Welcome to CodeWithDk now.</h1>")
    if request.COOKIES.get('visits'):
        html.set_cookie('CodeWithDk', 'Welcome Back')
        value = int(request.get('visits'))
        html.set_cookie('visits', value + 1)
    else:
        value = 1
        text = "Welcome for the first time."
        html.set_cookie('visits', value)
        html.set_cookie('CodeWithDk', text)
    # html = HttpResponse("<h1>Welcome to CodeWithDk</h1>")
    # html.set_cookie('CodeWithdk', 'We are setting a cookie for you.', max_age=None)
    return html


def showcookie(request):
    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        text = request.COOKIES.get('CodeWithDk')
        html = HttpResponse("<center><h1>{0}<br>You have requested this page {1} time.</h1></center>".format(text, value))
        html.set_cookie('visits', int(value)+1)
        return html
    else:
        return redirect('/setcookie')
    # show=request.COOKIES['CodeWithDk']
    # html = "<center> New Page <br>{0} </center>".format(show)
    # return HttpResponse(html)

def updating_cookie(request):
    html = HttpResponse("We are updating cookie which is set before.")
    html.set_cookie('CodeWithDk', 'Updated Successfully')
    return html

def deleting_cookie(request):
    html = HttpResponse("Deleting the cookie which is set")
    html.delete_cookie('CodeWithDk', 'Updated Successfully')
    return html