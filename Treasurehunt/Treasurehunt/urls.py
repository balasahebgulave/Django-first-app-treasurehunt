"""Treasurehunt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from Treasure.views import home
from Treasure.views import detail
from Treasure.views import add_new
from Treasure.views import customview
from Treasure.views import edit
from django.conf import settings
from django.conf.urls.static import static
from Treasure.views import loginform
from Treasure.views import logoutform


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home),
    path('detail/<int:val>/',detail),
    path('newtreasure/',add_new),
    path('custom/',customview),
    path('edit/<int:val>/',edit),
    path('login/',loginform),
    path('logout/',logoutform),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


