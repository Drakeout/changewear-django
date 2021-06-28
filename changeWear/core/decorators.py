from django.http import HttpResponse
from django.shortcuts import redirect

#code
def usuario_identificado(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_page')
        else: 
            return view_func(request, *args, **kwargs)

    return wrapper_func


def usuarios_permitiado(roles_permitidos=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in roles_permitidos:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('No tienes los permisos para ver esta página')
        return wrapper_func
    return decorator