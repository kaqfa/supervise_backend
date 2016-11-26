"""supervise_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from rest_framework import routers
from app.views import foo_view

# router = routers.DefaultRouter()
# router.register(r'users', foo_view)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^foo/', foo_view),
    url(r'^f/auth', foo_view),
    url(r'^f/createcomment', foo_view),
    url(r'^f/creatework', foo_view),
    url(r'^f/deletecomment', foo_view),
    url(r'^f/download', foo_view),
    url(r'^f/getallfield', foo_view),
    url(r'^f/getgraduated', foo_view),
    url(r'^f/gettask', foo_view),
    url(r'^f/getungraduated', foo_view),
    url(r'^f/getusername', foo_view),
    url(r'^f/isexist', foo_view),
    url(r'^f/resetpassword', foo_view),
    url(r'^f/search', foo_view),
    url(r'^f/searchfield', foo_view),
    url(r'^g/getlistthesis', foo_view),
    url(r'^s/claim', foo_view),
    url(r'^s/editprofil', foo_view),
    url(r'^s/get', foo_view),
    url(r'^s/getall', foo_view),
    url(r'^s/inputcode', foo_view),
    url(r'^s/propose', foo_view),
    url(r'^s/register', foo_view),
    url(r'^s/savethesis', foo_view),
    url(r'^su/addtask', foo_view),
    url(r'^su/claim', foo_view),
    url(r'^su/createtask', foo_view),
    url(r'^su/createtemplate', foo_view),
    url(r'^su/deletefield', foo_view),
    url(r'^su/deletetask', foo_view),
    url(r'^su/deletetemplate', foo_view),
    url(r'^su/editprofil', foo_view),
    url(r'^su/get', foo_view),
    url(r'^su/getall', foo_view),
    url(r'^su/getstudentprogress', foo_view),
    url(r'^su/issupervisor', foo_view),
    url(r'^su/register', foo_view),
    url(r'^su/removetask', foo_view),
    url(r'^su/response', foo_view),
    url(r'^su/savefield', foo_view),
    url(r'^su/updatetask', foo_view),
    url(r'^su/updatetasktemplate', foo_view),
    url(r'^su/updatetemplate', foo_view),
    url(r'^su/validation', foo_view),
]
