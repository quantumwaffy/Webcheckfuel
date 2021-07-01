from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def user_login(request):
    status = ""
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["pass"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/parsing")
            else:
                status = f"Disabled account for {username}"
        else:
            status = f"The user {username} does not exist or incorrect password"

    return render(request, "registration/login.html", {"status": status})
