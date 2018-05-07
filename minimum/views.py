
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from .models import *
from django.core.paginator import Paginator
from django.shortcuts import render, render_to_response
# Create your views here.



def list_news (request, page_number = 1):
	args = {}	
	all_news = News.objects.order_by('-date')
	current_page = Paginator(all_news, 35)
	args ['list_news'] = current_page.page(page_number)
	args['ads'] = Ads.objects.order_by('-date')[:1]
	return render_to_response('list_news.html', args)


def get_news(request, news_id = 1):
	args = {}
	args['get_news'] = News.objects.get(id = news_id)
	args['ads'] = Ads.objects.order_by('-date')[:1]

	
	return render_to_response('get_news.html', args)


def list_video (request, page_number = 1):
	args = {}	
	all_video = Video.objects.order_by('-date')
	current_page = Paginator(all_video, 15)
	args['ads'] = Ads.objects.order_by('-date')[:1]
	args['list_video'] = current_page.page(page_number)
	
	return render_to_response('list_video.html', args)

def list_faq (request):
	args = {}
	args['list_faq'] = Faq.objects.all

	return render_to_response('list_faq.html', args)


def hiros(request):
	args = {}
	args['heroes'] = Hiro.objects.all

	return render_to_response('heroes.html', args)


