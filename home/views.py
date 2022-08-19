from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect

# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('/login')

def home(request):
    return render(request, "home.html")
def auth_login(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)

        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            return redirect('/')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        return render(request, "login.html")