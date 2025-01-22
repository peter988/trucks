"""
URL configuration for trucks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from producs import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps import GenericSitemap  
from django.contrib.sitemaps.views import sitemap 
from django.views.generic.detail import DetailView
from producs.models import *
from django.shortcuts import get_object_or_404

class ServiceDetailView(DetailView):
    model = Category
    def get_object(self):
        # Retrieve the object using the 'name' field instead of 'pk' or 'slug'
        return get_object_or_404(Category, name=self.kwargs['name'])
    
    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        context = {}
        products =  Product.objects.filter(category=Category.objects.get(name=self.kwargs['name']))
        context['products'] = products  # Adding the dictionary to the context
        # print(products)
        return context
    
    def get_template_names(self):
        return [f'{self.object.name.replace(" ", "").lower().replace("-", "")}.html']

urlpatterns = [
    path("admin/", admin.site.urls),
    path('filters/', views.filters, name='pickup_trucks'),
    path('products/<str:name>/', ServiceDetailView.as_view(), name='service-detail'),
    path('categories/', views.cats, name='cats'),
    path('', views.main, name='main'),
    path('about-us/', views.aboutus, name='about_us'),
    path('contact-us/', views.contactus, name='contact_us'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)