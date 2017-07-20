# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.template import Context, RequestContext
from django.shortcuts import render_to_response, render

from core.jsonresponse import create_response, decode_json_str
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
# Create your views here.

# @login_required
def index(request):
    platform = Platform.objects.filter(source=1,is_default=1).first()
    platform_id = platform.id if platform else 0
    c = RequestContext(request, {
            'nav_name': 'index',
            'username': request.user.username,
            'id': platform_id
        })
    return render_to_response('platforms/index.html', c)

# @login_required
def get_platforms(request):
    items = []
    source_id = 1
    #for p in Platform.objects.filter(is_used=True).using("live"):
    for p in Platform.objects.filter(source=source_id):
        count = QMSPlatformLive.objects.filter(platform_id=p.id, is_used=True).count()
        if count > 0:
            items.append({
                "id": p.id,
                "name": p.name,
                "logo_url": p.logo_url,
                "count": count
                })
    print ">>>d",items
    items = sorted(items, key=lambda p:p['count'],reverse=True)
    response = create_response(200)
    response.data = {
        "items": items
    }
    return response.get_response()
# @login_required
def get_lives(request):
    id = request.POST.get('id', 1)
    source_id = 1
    items = []
    # print "<<<><<assss><",id
    # if source_id == 1:  
    for p in QMSPlatformLive.objects.filter(is_used=True, platform_id=id).order_by("-online_users"):
        if "rtmp" in p.url:
            type = "rtmp"
        elif "flv" in p.url:
            type = "flv"
        elif "m3u8" in p.url:
            type = "m3u8"
        elif  p.url.find(".mp4") > -1 or p.url.find(".MP$") > -1:
            type = "mp4"
        items.append({
                "id":p.id,
                "name":p.zhubo_name if len(p.zhubo_name) <= 3 else p.zhubo_name[:3],
                "header_img":p.header_img,
                "count": p.online_users,
                "id":p.id,
                "type": type,
                "live_url": ""
                })
    # else:

    #     try:
    #         request_id = PlatformLive.objects.filter(platform_id=id).using("live").order_by("-request_id").first().request_id
    #     except:
    #         request_id = None
    #     print ">>>DD>D>D>D>D>D>D>",request_id
    #     if request_id:
    #         for p in PlatformLive.objects.filter(platform_id=id, request_id=request_id).using("live").order_by('-id'):
    #             print p.id,"<<<<<"
    #             if p.rtmp_url:
    #                 p.live_url = p.rtmp_url
    #                 p.type="rtmp"
    #             elif p.flv_url:
    #                 p.live_url = p.flv_url
    #                 p.type="flv"
    #             elif p.m3u8_url:
    #                 p.live_url = p.m3u8_url
    #                 p.type="m3u8"
    #             else:
    #                 print ">>>>>>?"
    #                 continue
    #             items.append({
    #                 "id":p.id,
    #                 "name":p.zhubo_name,
    #                 "header_img":p.header_img,
    #                 "count": p.online_users,
    #                 "id":p.id,
    #                 "type": p.type,
    #                 "live_url": p.live_url
    #                 })
    # print "?>>>>>",items
    response = create_response(200)
    response.data = {
        "items": items
    }
    return response.get_response()

def get_live(request):
    print request.user.is_authenticated()
    # if not request.user.is_authenticated():
    #     response = jsonresponse.create_response(201, u"请登录")
    #     return response

    # if not request.user.is_active:
    #     response = jsonresponse.create_response(201, u"帐号过期")
    #     return response
    response = create_response(200)


    id = request.POST.get("id", None)
    data = {}
    if id:
        live = QMSPlatformLive.objects.filter(id=id).first()
        if live:
            data = {
                "live_url": live.url
            }
    response.data = data
    return response.get_response()


