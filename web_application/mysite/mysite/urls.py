"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path, re_path
from mysite import views

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import handler400, handler404, handler500
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    # add these to configure our home page (default view) and result web page
    path('input/', views.input, name='input'),
    path('result/', views.result, name='result'),
    path('index/',views.index, name='index'),
    path('map/', views.map, name='map'),
    path('contact/',views.contact, name='contact'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT})
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)


handler400 = 'mysite.views.bad_request'
handler404 = 'mysite.views.page_not_found'
handler500 = 'mysite.views.server_error'
