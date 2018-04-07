"""shushratHospital URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from hospital import views as hospital


login_urlpatterns = [
    url(r'^$', hospital.loginuser, name='login'),
    url(r'^logout$', hospital.logout_view, name='logout'),
    url(r'^singup', hospital.singupuser, name='singupuser'),
]


odp_urlpatterns = [
    url(r'^$', hospital.newopd, name='newopd'),
    url(r'^show$', hospital.showopd, name='showopd'),
]

patiente_urlpatterns = [
    url(r'^$', hospital.newpatiente, name='newpatiente'),
    url(r'^show$', hospital.showpatiente, name='showpatiente'),
    url(r'^new$', hospital.newpatienteshow, name='newpatienteshow'),
    url(r'^disease', hospital.showdiseas, name='showdiseas'),
    url(r'^barcode$', hospital.patientebracode, name='patiente-bracode'),
]

ipd_urlpatterns = [
    url(r'^$', hospital.newipd, name='newipd'),
    url(r'^show$', hospital.showipd, name='showipd'),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'opd/', include(odp_urlpatterns)),
    url(r'ipd/', include(ipd_urlpatterns)),
    url(r'patiente/', include(patiente_urlpatterns)),
    url(r'', include(login_urlpatterns)),
]