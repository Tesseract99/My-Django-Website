from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  #just this will do all the saving work of the user
            username=form.cleaned_data.get('username')
            messages.success(request,f'Your acoount has been created!Please login.')
            return redirect('Login')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

#only people logged in must be able to edit posts
#so we make this fn
@login_required #this is a decorator--this prvents any person from entering the profile page even if he types /profile in url bar
def profile(request):
    return render(request,'users/profile.html')
