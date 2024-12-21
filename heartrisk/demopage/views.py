from django.shortcuts import render

# Create your views here.

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
 
def index(request):
    return render(request, 'index.html') 
def index(request):
    if(request.method == "POST"):
        #two inputs from the users, we need to store those inputs in our function
        username1 = request.POST['username']
        password1 = request.POST['password']
        user = authenticate(request,username=username1,password=password1)
        #authenticate() is used to connect with our auth_user table in our database and it will check with our user input valeus
        # if th username and password matches, it will return the username as result
        # if the username and password doesn't match, it will return the result as None.
        if(user != None):
            print("Login Successfull!!!")
        else:
            print("Error in Login")
    else:
        form = AuthenticationForm()
        #AuthenticationForm() is used to create a form with predefined options of username and password
        #form variable will have a html code for our username and password
        return render(request,'login.html',{'form':form})
        #if you need to pass these variables, we can pass only as tokens, so first create the tokens in login.html form tag.