from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method =="POST":
        form= UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegistrationForm()
    context = {"form": form, "title": "Register User"}
    return render(request,"accounts/register.html",context=context,)  

@login_required 
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect("user-profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context={
        "u_form":u_form,
        "p_form":p_form, 
        "title":"User Profile"


    }

    return render(request,'accounts/profile.html')
# Create your views here.
