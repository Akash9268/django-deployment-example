from django.shortcuts import render
from basic_app.forms import UserForm,userprofileinfoForm


#
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
	return render(request,'basic_app/index.html')

@login_required
def special(request):
	return HttpResponse("you are loggen in!")

@login_required  ##only logout when u r logged in
def user_logout(request):
	logout(request)

	return HttpResponseRedirect(reverse('index'))




def register(request):

	registered= False

	if request.method == "POST":
		user_form = UserForm(data=request.POST)
		profile_form = userprofileinfoForm(data=request.POST)


		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()
			user.set_password(user.password) ##set_password method is for hashing
			user.save()

			profile = profile_form.save(commit=False)

			profile.user  = user  ##defining one to one relationship when we have already declared in the out models.py

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']


			profile.save()

			registered = True

		else:
			print(user_form.errors,profile_form.errors)


	else:
		user_form = UserForm()
		profile_form = userprofileinfoForm()

	return render(request,'basic_app/registeration.html',
		{'user_form':user_form,
		  'profile_form':profile_form,
		  'registered':registered})



def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'basic_app/login.html', {})