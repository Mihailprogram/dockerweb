from . import views
from django.urls import include, path

app_name = 'viewapp'

urlpatterns = [ 
    path('', views.index, name='bot'),
  
]