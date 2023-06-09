#from django.urls import path
#from . import views


#app_name='home'



#urlpatterns = [
 #   path('', views.home_list, name='home_list'),
  #  ]



from django.urls import path
from . import views

app_name='home'


urlpatterns = [
    path('', views.home_list, name='home_list'),
    ]
