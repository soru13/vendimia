"""vendimia URL Configuration

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

from django.conf.urls import url,include
from django.contrib import admin

from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^ventas/', include('ventas.urls', namespace='ventas')),
	url(r'^articulos/', include('articulos.urls', namespace='articulos')),
	url(r'^admin/', include(admin.site.urls)),

# Python Social Auth URLs
# url('', include('social.apps.django_app.urls', namespace='social')),


# Login URL
url(r'^login/$', auth_views.LoginView.as_view(template_name="users/login.html"),name="login"),

# Logout URL
url(r'^logout/$',auth_views.logout,{'next_page':'/login'},name='logout'),
url(r'^',include('users.urls', namespace='usuarios')),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)