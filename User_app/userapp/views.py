from django.http import HttpResponse
from django.shortcuts import render

from userapp.models import UserInfo

def index(request):
	latest_user_list = UserInfo.objects.order_by('-create_date')
	context = {'latest_user_list': latest_user_list}
	return render(request, 'userapp/index.html', context)

def detail(request, user_id):
	userinfo = get_object_or_404(UserInfo, pk=user_id)
	return render(request, 'userapp/detail.html', {'userinfo': userinfo})



