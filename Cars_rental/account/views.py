from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm,UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            messages.success(request,'Your account '+ str(new_user) +' has been successfully created.')
            return render(request,'account/register.html',{'user_form': user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html',{'user_form': user_form})

def user_login(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        #form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return HttpResponse('Authenticated successfully')
                else:
                    messages.warning(request,'Disabled account')
                    # return HttpResponse('Disabled account')
            else:
                messages.error(request,'Invalid login')
                # return HttpResponse('Invalid login')
        else:
            form = LoginForm()
        return render(request, 'account/login.html', {'form': form})
    return render(request,'account/login.html',{'form':form})


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request,'You logged out now, you can login here again')
    return redirect('login')