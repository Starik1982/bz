from django.conf.urls import url, include
from minimum import views



urlpatterns = [
	url(r'^get/(?P<news_id>\d+)/$', views.get_news, name ='watched_news'),
	url(r'^videolist/(\d+)/$', views.list_video, name ='list_video'),
    url(r'^(\d+)/$', views.list_news, name ='list_news'),
    url(r'^1/$', views.list_news, name ='list_news'),
    url(r'^get_hiro/$', views.hiros, name ='list_hiros'),
    url(r'^$', views.list_faq, name ='faq'),

]