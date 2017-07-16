"""climate (about us) URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from . import views
from . import about_us_views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^', include('climateApp.urls')),
    url(r'^utpl$', about_us_views.UTPLAboutUsView.as_view(), name="about-us-utpl"),
    url(r'^sbc$', about_us_views.SBCAboutUsView.as_view(), name="about-us-sbc"),
    url(r'^madba$', about_us_views.MADBAAboutUsView.as_view(), name="about-us-madba"),
    url(r'^nsed$', about_us_views.NSEDAboutUsView.as_view(), name="about-us-nsed")
]