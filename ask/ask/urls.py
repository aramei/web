"""ask URL Configuration

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', qa.view.test, name='home'),
    path('login/', qa.view.test, name='login'),
    path('signup/', qa.view.test, name='signup'),
    path('question/<int:id>/', qa.view.test, name='question'),
    path('ask/', qa.view.test, name='ask'),
    path('popular/', qa.view.test, name='popular'),
    path('new/', qa.view.test, name='new'),
]
