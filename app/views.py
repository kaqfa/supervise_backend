"""Ini adalah modul untuk urusan yang hubungannya dengan aplikasi"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from app.models import Application
from rest_framework import status


@api_view(['GET', 'POST'])
def foo_view(request):
    """Ini cuman fungsi latihan aja untuk memastikan jalan"""
    if request.method == 'POST':
        return Response({'code':'2', 'message':'this is just a foo POST',
                         'data':request.data})
    return Response({'code':'1', 'message':'this is just a foo', 'data':'no data in get'})

def app_key_required(function):
        
    def decorator(request, *args, **kwargs):
        try:
            Application.objects.get(code=request.data['appkey'])
        except KeyError:            
            return Response({'code':'0', 'message':'appkey must present'})
        except Application.DoesNotExist:
            del request.data['appkey']
            return Response({'code':'0', 'message':'appkey is not valid'})
            
        return function(request, data=request.data, *args, **kwargs)

    return decorator


class AppKeyMixin(object):
    
    def appkey_check(self, reqdata):
        try:
            Application.objects.get(code=reqdata['appkey'])
        except KeyError:            
            return Response({'code':'0', 'message':'appkey must present'})
        except Application.DoesNotExist:
            del reqdata['appkey']            
            return Response({'code':'0', 'message':'appkey is not valid'})

        return False


class RegisterApp(viewsets.ViewSet):
    """ViewSet untuk mendaftarkan aplikasi"""

    def create(self, request):
        resp = {}
        try:
            result = Application.register_application(request.data['AppName'])
        except KeyError:
            resp = {'code': '-1', 'message': 'Missing AppName parameter'}
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)

        if result is False:
            resp = {'code': '0', 'message':'appname exists'}
            return Response(resp, status=status.HTTP_409_CONFLICT)
        else:
            resp = {'code': '1', 'message': result}
            return Response(resp, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_thesis_list(request):
    """*appkey"""
    if request.method == 'POST':
        return Response({'code':'2', 'message':'this is just a foo POST',
                         'data':request.data})
    return Response({'code':'1', 'message':'this is just a foo', 'data':'no data in get'})

@api_view(['GET'])
def search_expertise(request):
    """*appkey, *token, *keysearch"""
    return Response({'code':'1', 'message':'the message', 'data':'the fields'})

@api_view(['GET'])
def get_all_expertise(request):
    """*appkey, *token"""
    return Response({'code':'1', 'message':'the message', 'data':'all fields'})

@api_view(['GET'])
def download_file(request):
    """*file_id"""
    return Response({'file':'the file'})
    