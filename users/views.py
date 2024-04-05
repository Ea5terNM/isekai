from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render 
from django.http import HttpRequest, HttpResponseRedirect
from users.forms import RegisterForm ,UserProfilesForm ,ExtendedProfilesForm
from django.contrib import messages




def register (request: HttpRequest):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return HttpResponseRedirect(reverse("Home"))
    else:
        form = RegisterForm()
    context = {"form": form}
    return render (request,"users/register.html", context)

@login_required
def dashboard (request: HttpRequest):
    return render (request,"users/dashboard.html")


@login_required
def profile(request: HttpRequest):
    user = request.user

    # POST
    if request.method == "POST":
        form = UserProfilesForm(request.POST, instance=user)
        is_new_profile = False
        try:
            # Will be updated profile
            extended_form = ExtendedProfilesForm(request.POST, instance=user.profile)
        except:
            # Will be created profile
            is_new_profile = True
            extended_form = ExtendedProfilesForm(request.POST)

        if form.is_valid() and extended_form.is_valid():
            form.save()
            if is_new_profile:
                # Create profile
                profile = extended_form.save(commit=False)
                profile.user = user
                profile.save()
            else:
                # Update profile
                extended_form.save()
            return HttpResponseRedirect(reverse("profile"))
    else:
        form = UserProfilesForm(instance=user)
        try:
            extended_form = ExtendedProfilesForm(instance=user.profile)
        except:
            extended_form = ExtendedProfilesForm()

    # GET
    context = {
        "form": form,
        "extended_form": extended_form
    }
    return render(request, "users/profile.html", context)

def shopp (request):
    return render (request,"users/shopping_cart.html")










