# -*- coding: utf-8 -*-

__author__ = "bert"
import json
from django.conf import settings
#===============================================================================
# RestfulUrlMiddleware : 处理request.path_info的middleware
#===============================================================================
class AllowMiddleware(object):
    def process_request(self, request):
        path_info = request.path_info
        if path_info.startswith("/"):
            pos = path_info.find('/', 2)
            app = str(path_info[:pos+1])

            # method = request.META['REQUEST_METHOD']
            # if method == 'POST' and '_method' in request.REQUEST:
            #     _method = request.REQUEST['_method']
            #     method = _method.upper()
            method = request.method.upper()

            request.original_path_info = path_info
            if len(path_info) == 1:
                pass #不处理path为/的情况
            elif path_info[-1] == '/':
                request.path_info = '%s%s' % (path_info, method)
            else:
                request.path_info = '%s/%s' % (path_info, method)
            try:
                if request.method in ["POST", "PUT"]:
                    request.body_data =  json.loads(request.body)
                else:
                    request.body_data =  {}
            except:
                request.body_data =  {}

        return None

    def process_response(self, request, response):
        print ">>>>>>"
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "PUT, DElETE, POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"

        return response