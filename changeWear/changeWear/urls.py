"""changeWear URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from pages.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Url de toda la aplicación, incluyendo la api
    path('', home_page, name='home_page'),
    path('mujer/', mujer_page, name='mujer_page'),
    path('hombre/', hombre_page, name='hombre_page'),
    path('ninos/', nino_page,name='nino_page'),
    path('producto/<str:pk>/', producto_page, name='producto_page'),

    path('registrarse/', registrarse_page, name='registrarse_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_user, name='logout_user'),
    path('carro/', carro_page, name='carro_page'),
    path('direccion/<str:pk>', direccion_page, name='direccion_page'),
    path('pagar/', pagar_page, name='pagar_page'),
    path('update_item/', updateItem, name='update_item'),
    path('user/<action>/', user_page, name='user_page'),

    path('vision/', vision_page, name='vision_page'),
    path('contacto/', contacto_page, name='contacto_page'),
    path('empleo/', empleo_page, name='empleo_page'),

    # api
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
