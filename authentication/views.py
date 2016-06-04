from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext

from articles.views import index
from authentication.forms import SigninForm, SignupForm

from authentication.models import CommonUser

def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                return render(request, 'signin.html', {'form':form})
        else:
            return redirect('/auth/signin')
    else:
        form = SigninForm()
        return render_to_response('signin.html',{'form':form}, context_instance=RequestContext(request))


def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			email = request.POST.get('email', '')
			username = request.POST.get('username', '')
			password = request.POST.get('password1', '')
			u = User.objects.create_user(username=username, email=email, 
				password=password)
			u.save()
			user = CommonUser(user=u)
			user.save()
			return redirect('/auth/signin')
		else:
			return render_to_response('signup.html', {'form':form},
				context_instance=RequestContext(request))
	else:
		form = SignupForm()
		return render_to_response('signup.html', {'form':form},
			context_instance=RequestContext(request))





def logout(request):
    auth.logout(request)
    return redirect('/')


