"""
URL configuration for erptools project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home import views
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path('dash/', views.dashboard),
    #path('employee/', views.employeeApiview.as_view()),
    # url("employee/",views.employeeApiview.as_view()),
    path('forcast/', include('inventory.urls')),
    path('final/', include('myapi.urls')),
    path('app/', include('myapp.urls')),
    path('cor/', include('testing.urls')),
    
    
]
