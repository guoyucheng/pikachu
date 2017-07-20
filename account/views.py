# -*- coding: utf-8 -*-

from django.contrib import auth
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.template import Context, RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404
# from core.jsonresponse import create_response, decode_json_str
from core import jsonresponse
from account.models import CustomUserSession

def logout(request):
    auth.logout(request)
    response = jsonresponse.create_response(200)
    response.data = {
    }
    response = response.get_response()
    return response

def login(request):
    """
    登录首页
    """
    print ">>>>>>>sdfa"
    username = request.POST.get('username', 'empty_username')
    password = request.POST.get('password', 'empty_password')
    user = auth.authenticate(username=username, password=password)
    if user:
        if user.is_active:
            auth.login(request, user)

            session_keys = [session.session_key for session in CustomUserSession.objects.filter(user=user)]
            if session_keys:
                Session.objects.filter(session_key__in=session_keys).delete()
                CustomUserSession.objects.filter(session_key__in=session_keys).delete()
            CustomUserSession.objects.create(session_key=request.session.session_key,user=user)

            response = jsonresponse.create_response(200)
            response.data = {
                "user": {
                    "name": user.username
                }
            }
            response = response.get_response()
        else:
            response = jsonresponse.create_response(201, u"帐号已过期")
    else:
        response = jsonresponse.create_response(202, u"用户名或密码错误")
    return response