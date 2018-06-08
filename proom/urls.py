from django.conf.urls import url, include
from proom import views



urlpatterns = [
	
    url(r'^(?P<personal_room_id>\d+)/$', views.personal_room, name ='room'),

]
