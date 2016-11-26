"""Ini adalah modul untuk urusan yang hubungannya dengan aplikasi"""

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def foo_view(request):
    """Ini cuman fungsi latihan aja untuk memastikan jalan"""
    if request.method == 'POST':
        Response({'code':'2', 'message':'this is just a foo POST', 'data':'POST data applied'})
    return Response({'code':'1', 'message':'this is just a foo', 'data':'no data applied'})
