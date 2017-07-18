"""climate URL Configuration

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

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^', include('climateApp.urls')),
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^datos/$', views.DataView.as_view(), name="datos"),
    url(r'^datos/def-vocab$', views.VocabDefView.as_view(), name="def-vocab"),
    url(r'^vocab/$', views.RDFView.as_view(), name="rdf-vocab"),
    url(r'^graficos/$', views.GraphView.as_view(), name="graficos"),
    url(r'^graficos/cont-bruta$', views.BruteContaminationGraphView.as_view(), name="grafico-cont-bruta"),
    url(r'^graficos/per-capita$', views.PerCapitaContaminationGraphView.as_view(), name="grafico-per-capita"),
    url(r'^graficos/renov-prod$', views.RenewableEnergyProductionGraphView.as_view(), name="grafico-renov-prod"),
    url(r'^graficos/renov-cons$', views.RenewableEnergyProductionGraphView.as_view(), name="grafico-renov-cons"),
    url(r'^graficos/sf6-emissions$', views.GasFS6emissionsGraphView.as_view(), name="grafico-GasFS6emissions"),
    url(r'^graficos/p-co2-gas-emi$', views.CO2GaseousFuelPGraphView.as_view(), name="grafico-CO2GaseousFuelP"),
    url(r'^graficos/b-co2-gas-emi$', views.CO2GaseousFuelBGraphView.as_view(), name="grafico-CO2GaseousFuelB"),
    url(r'^graficos/p-co2-liq-emi$', views.CO2LiquidFuelPGraphView.as_view(), name="grafico-CO2LiquidFuelP"),
    url(r'^graficos/b-co2-liq-emi$', views.CO2LiquidFuelBGraphView.as_view(), name="grafico-CO2LiquidFuelB"),
    url(r'^graficos/b-co2-sld-emi$', views.CO2SolidFuelBGraphView.as_view(), name="grafico-CO2SolidFuelB"),
    url(r'^graficos/estadisticas$', views.StatisticsGraphView.as_view(), name="grafico-estadisticas"),
    url(r'^acerca_de/', include('climateApp.about_us_urls'))
]
