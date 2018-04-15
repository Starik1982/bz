from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from bg_result.models import BgResult
from guild_members.models import GuildMembers
from minimum.models import News, Video, Ads
from datetime import date



# Create your views here.
def main(request):
	quantity = GuildMembers.objects.all()
	a = 0
	for i in  quantity:
		a = a + 1	

	
	args = {}	
	args['video'] = Video.objects.order_by('-date')[:4]
	args['bg_results'] = BgResult.objects.order_by('-bg_date', '-result')[:a]
	args['news'] = News.objects.order_by('-date')[:5]
	args['ads'] = Ads.objects.order_by('-date')[:1]
	return render_to_response('articles.html', args)



	

