from django.conf.urls import url, include
from proom import views



urlpatterns = [
    url(r'^$', views.personal_room, name ='room'),

]
