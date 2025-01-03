"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,URLPattern, include
from example import views  # Import the home app views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    
    path('services', views.services, name='services'),  
    path('industries', views.industries, name='industries'),
    path('technologies', views.technologies, name='technologies'),
    path('company', views.company, name='company'),     
    path('work', views.work, name='work'), 
    path('clients', views.clients, name='clients'), 
    path('blog', views.blog, name='blog'),      
    path('about-us', views.about_us, name='about_us'),
    path('contact-us', views.contact_us, name='contact'),  
    path('lets-talk', views.lets_talk, name='lets_talk'),
    path('success', views.success_view, name='success'),    
     
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)