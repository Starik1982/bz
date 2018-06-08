from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from .models import *
from django.contrib import auth
from bg_result.models import BgResult

# Create your views here.
def personal_room(request, personal_room_id):	
	args = {}
	this_model = PersonalRoom.objects.get(id = personal_room_id)
	gild_mamber_id = this_model.gild_mamber.id
	a = auth.get_user(request).id
	personal_room_id = PersonalRoom.objects.get(user_id = a)

	args['bg_result'] = BgResult.objects.filter(nickname = gild_mamber_id)
	args['room'] = PersonalRoom.objects.get(id = personal_room_id.id)
	args['username'] = auth.get_user(request).username
	
	print(personal_room_id.id)

	

	


	return render_to_response('proom.html', args)