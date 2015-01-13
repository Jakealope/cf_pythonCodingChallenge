from django.shortcuts import render
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from userapp.models import UserInfo


class UserForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['id', 'f_name', 'l_name', 'email']


def index(request):
    if request.method == 'POST':
        userinfo = UserForm(request.POST)
    	if userinfo.is_valid():
    		userinfo.save()
    return render(request, 'userapp/index_base.html', {
        'users': UserInfo.objects.order_by('id'),
    })


def detail(request, id):
    try:
        user = UserInfo.objects.get(pk=id)
        form = UserForm(instance=user)
    except UserInfo.DoesNotExist:
        raise Http404
    return render(request, 'userapp/detail.html', {
        'user': user,
        'form': form,
    })


def update(request, id):
    if request.method == 'POST':
        user = UserInfo.objects.get(pk=id)
        userinfo = UserForm(request.POST)
        if userinfo.is_valid():
            user.f_name = request.POST['f_name']
            user.l_name = request.POST['l_name']
            user.email = request.POST['email']
            user.save()
        return HttpResponseRedirect('/userapp/')


def delete(request, id):
    user = UserInfo.objects.get(pk=id)
    user.delete()
    return HttpResponseRedirect('/userapp/')    
