# coding: utf-8
from users.models import User
from users.forms import UserEditForm, UserCreateForm
from django.shortcuts import (render, get_object_or_404,
                              HttpResponseRedirect, Http404,)
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
def profile(request):
    user = User.objects.get(pk=request.user.id)
    context = {
        'profile': user,
    }
    return render(request, 'users/profile.html', context)


@login_required
def edit_profile(request):
    user = request.user
    form = UserEditForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(
            reverse('index')
        )
    return render(request, 'users/edit_user.html', {'form': form})


def user_list(request):
    listing = User.objects.order_by('-id')
    context = {
        'user_list': listing,
    }
    return render(request, 'users/user_list.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url='/error404', redirect_field_name='')
def admin_profile(request, user):
    user = get_object_or_404(User, id=user)
    context = {
        'profile': user
    }
    return render(request, 'users/admin_profile.html', context)


def register(request, autologin=True):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('users:profile'))
    form = UserCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        if autologin:
            username = form.cleaned_data['login']
            password = form.cleaned_data['password2']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'users/register.html', {'form': form})
