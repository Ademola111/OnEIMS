from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from OnEIMS_users.forms import Userform, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'OnEIMS_users/home.html')


def register(request):

    registered = False

    if request.method == "POST":
        user_form = Userform(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            
            registered = True
        

        #else:
            #print(user_form.error, profile_form.error)
    
    else:
        user_form = Userform()
        profile_form = UserProfileForm()
       
    return render(request, 'OnEIMS_users/register.html', {'user_form':user_form,
            'profile_form':profile_form,
            'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account is deactivated')
        else:
            return HttpResponse('Please enter the correct Username and Password')
    
    else:
        return render(request, 'OnEIMS_users/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))