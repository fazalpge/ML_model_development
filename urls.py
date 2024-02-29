from . import views
from django.urls import include, path

urlpatterns = [
    #path('read/', views.read),
    path('show/', views.show,name='showemp'),
    path('data/', views.predict_attrition,name='showdata'),
]