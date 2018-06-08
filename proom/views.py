from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from .models import *
from django.contrib import auth
from bg_result.models import BgResult


def personal_room(request):	
	args = {}
	user_id = auth.get_user(request).id  						# get user id
	personal_room = PersonalRoom.objects.get(user_id = user_id)	# get related this user PersonalRoom models
	args['bg_result'] = BgResult.objects.filter(nickname = personal_room.gild_mamber.id)
	args['room'] = PersonalRoom.objects.get(id = personal_room.id)
	args['username'] = auth.get_user(request).username
	print(personal_room)

	return render_to_response('proom.html', args)

