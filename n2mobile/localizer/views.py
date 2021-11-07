from django.forms import fields
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.gis.geos import Point
from django.contrib.gis.geos import fromstr
from django.views import generic
from django.contrib.gis.db.models.functions import Distance
from .models import Marker


latitude = 32.77238845369153
longitude = 39.90940704430817


user_location = Point(latitude,longitude, srid=4326)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        form = CreateUserForm()
    
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
          
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
            else:
                messages.info(request, 'Your Password is too short or commanly, Your password must contain at least 8 characters ')
        context = {'form': form}
        return render(request, 'localizer/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                messages.info(request, 'Username or Password is incorrect')
            
        context={} 
        return render(request, 'localizer/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

class Home(generic.ListView):

    model = Marker
    context_object_name = 'markers'
    queryset = Marker.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:6]
    template_name = 'localizer/main.html'

home = Home.as_view()

 