"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
# include function allows referencing other URLconfis

# You should always use include() when you include other URL patterns
# admin.site.urls is the only exception to this
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    # The following two path are different, they're accesible by:
    # 1. localhost/polls/insidefirst, localhost/polls/insidesecond, localhost/polls/insidethird
    # 2. localhost/polls/inside/first, localhost/polls/inside/second, localhost/polls/inside/third
    # path('polls/inside', include('polls.urls')), 
    # path('polls/inside/', include('polls.urls')),
]