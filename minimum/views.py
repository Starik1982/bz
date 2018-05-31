
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from .models import *
from django.core.paginator import Paginator
from django.shortcuts import render, render_to_response
from django.contrib import auth

# Create your views here.



def list_news (request, page_number = 1):
	args = {}	
	all_news = News.objects.order_by('-date')
	current_page = Paginator(all_news, 35)
	args ['list_news'] = current_page.page(page_number)
	args['ads'] = Ads.objects.order_by('-date')[:1]
	args['username'] = auth.get_user(request).username
	return render_to_response('list_news.html', args)


def get_news(request, news_id = 1):
	args = {}
	args['get_news'] = News.objects.get(id = news_id)
	args['ads'] = Ads.objects.order_by('-date')[:1]
	args['username'] = auth.get_user(request).username

	
	return render_to_response('get_news.html', args)


def list_video (request, page_number = 1):
	args = {}	
	all_video = Video.objects.order_by('-date')
	current_page = Paginator(all_video, 15)
	args['ads'] = Ads.objects.order_by('-date')[:1]
	args['list_video'] = current_page.page(page_number)
	args['username'] = auth.get_user(request).username
	
	return render_to_response('list_video.html', args)

def list_faq (request):
	args = {}
	args['list_faq'] = Faq.objects.all
	args['ads'] = Ads.objects.order_by('-date')[:1]
	args['username'] = auth.get_user(request).username

	return render_to_response('list_faq.html', args)


def hiros(request):
	args = {}
	args['heroes'] = Hiro.objects.all
	args['ads'] = Ads.objects.order_by('-date')[:1]
	args['username'] = auth.get_user(request).username

	return render_to_response('heroes.html', args)


def get_hiro(request, hiro_id = 1):
	
	args = {}
	args['get_hiros'] = Hiro.objects.get(id = hiro_id)
	args['ads'] = Ads.objects.order_by('-date')[:1]
	args['username'] = auth.get_user(request).username
	print()

	
	return render_to_response('get_hiro.html', args)


def list_talant(request):
	args = {}
	args['talents'] = Talent.objects.all
	args['ads'] = Ads.objects.order_by('-date')[:1]
	args['username'] = auth.get_user(request).username

	return render_to_response('list_talant.html', args)

def get_talant(request, talent_id = 1):
	args = {}
	args['talent'] = Talent.objects.get(id = talent_id)
	args['ads'] = Ads.objects.order_by('-date')[:1]
	args['username'] = auth.get_user(request).username

	return render_to_response('get_talant.html', args)





