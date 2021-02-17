from django.contrib import admin
from django.urls import include, path

from code import views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
]
