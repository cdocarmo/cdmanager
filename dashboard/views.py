# coding=UTF-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from usuarios.forms import *

from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def index(request):
	return render_to_response('index.html', locals(),
		  context_instance=RequestContext(request))    



def ingresar(request):
	if request.method == 'POST':
		formulario = LoginForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password1']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/')
				else:
					error = u'Usuario no Activo, consulte Administrador...'
					return render_to_response('usuario/login.html',
						{'formulario':formulario,
						'error':error}, 
						context_instance=RequestContext(request))
			else:
					error = u'Usuario o contraseña incorrecta, intente nuevamente.'
					return render_to_response('usuario/login.html',
						{'formulario':formulario,
						'error':error}, 
						context_instance=RequestContext(request))
	else:
		formulario = LoginForm()
	return render_to_response('usuario/login.html',
		{'formulario':formulario}, 
		context_instance=RequestContext(request))


@login_required(login_url='/login')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')  	