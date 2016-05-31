from django.contrib import auth
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext

from articles.views import index
from authentication.forms import SigninForm


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
            return render_to_response('signin.html', context_instance=RequestContext(request))
    else:
        form = SigninForm()
        return render_to_response('signin.html',{'form':form}, context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    return redirect('/')


