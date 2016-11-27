"""Ini adalah modul untuk urusan yang hubungannya dengan aplikasi"""

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def foo_view(request):
    """Ini cuman fungsi latihan aja untuk memastikan jalan"""
    if request.method == 'POST':
        return Response({'code':'2', 'message':'this is just a foo POST',
                         'data':request.data})
    return Response({'code':'1', 'message':'this is just a foo', 'data':'no data in get'})

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
    