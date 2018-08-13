from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        new_user = UserCreationForm(data=request.POST)
        if new_user.is_valid():
            new_user.save()
            authenticated_user = authenticate(username=new_user.cleaned_data.get('username'),
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse("learning_logs:index"))
        else:
            print(new_user.error_messages)
            form = UserCreationForm(new_user.error_messages)
    context = {"form": form}
    return render(request, "users/register.html", context)
