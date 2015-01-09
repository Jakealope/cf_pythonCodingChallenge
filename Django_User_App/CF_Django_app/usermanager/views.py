from django.shortcuts import render
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from usermanager.models import UserManager


class UserForm(ModelForm):
    class Meta:
        model = UserManager
        fields = ['id', 'firstname', 'lastname', 'email']


def index(request):
    if request.method == 'POST':
        userinfo = UserForm(request.POST)
        if userinfo.is_valid():
            userinfo.save()
    return render(request, 'base_site.html', {
        'users': UserManager.objects.order_by('id'),
    })


def detail(request, id):
    try:
        user = UserManager.objects.get(pk=id)
        form = UserForm(instance=user)
    except UserManager.DoesNotExist:
        raise Http404
    return render(request, 'detail.html', {
        'user': user,
        'form': form,
    })


def update(request, id):
    if request.method == 'POST':
        user = UserManager.objects.get(pk=id)
        userinfo = UserForm(request.POST)
        if userinfo.is_valid():
            user.fname = request.POST['firstname']
            user.lname = request.POST['lastname']
            user.email = request.POST['email']
            user.save()
        return HttpResponseRedirect('/usermanager/')


def delete(request, id):
    user = UserManager.objects.get(pk=id)
    user.delete()
    return HttpResponseRedirect('/usermanager/')