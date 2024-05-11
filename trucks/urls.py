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

urlpatterns = [
    path("admin/", admin.site.urls),
    path('filters/', views.filters, name='pickup_trucks'),
    path('bushing/', views.bushing, name='bushing'),
    path('insulator/', views.insulator, name='insulator'),
    path('engine-mounting/', views.engine_mounting, name='engine_mounting'),
    path('center-bearing/', views.center_bearing, name='center_bearing'),
    path('torque-bushing/', views.torque_bushing, name='torque_bushing'),
    path('equaliser-hutch/', views.equaliser_hutch, name='equaliser_hutch'),
    path('equaliser-bush/', views.equaliser_bush, name='equaliser_bush'),
    path('bolt-repair-kit-for-equaliser/', views.bolt_repair_kit_for_equaliser, name='bolt_repair_kit_for_equaliser'),
    path('cabin-mounting/', views.cabin_mounting, name='cabin_mounting'),
    path('radiator-mounting/', views.radiator_mounting, name='radiator_mounting'),
    path('bronze-bushing-trunnion/', views.bronze_bushing_trunnion, name='bronze_bushing_trunnion'),
    path('brass-washer-for-trunnion/', views.brass_washer_for_trunnion, name='brass_washer_for_trunnion'),
    path('trunnion/', views.trunnion, name='trunnion'),
    path('brass-washer-for-trunnion-4/', views.brass_washer_for_trunnion_4, name='brass_washer_for_trunnion_4'),
    path('spring-mounting/', views.spring_mounting, name='spring_mounting'),
    path('torque-rod/', views.torque_rod, name='torque_rod'),
    path('spring-bushing/', views.spring_bushing, name='spring_bushing'),
    path('torque-rod-bush/', views.torque_rod_bush, name='torque_rod_bush'),
    path('king-pin/', views.king_pin, name='king_pin'),
    path('torque-bush/', views.torque_bush, name='torque_bush'),
    path('equaliser-bush/', views.equaliser_bush, name='equaliser_bush'),
    path('categories/', views.cats, name='cats'),
    path('', views.main, name='main'),
    path('about-us/', views.aboutus, name='about_us'),
    path('contact-us/', views.contactus, name='contact_us'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)