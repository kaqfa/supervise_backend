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
from rest_framework import routers
from app.views import foo_view
import app.views as appview
import progress.views as progviews
import member.views as memviews

router = routers.DefaultRouter()
# router.register(r'users', foo_view)
router.register(r'g/app', appview.RegisterApp, base_name='register-app')
router.register(r's/register', memviews.StudentRegister, base_name='student-register')
router.register(r'su/register', memviews.SupervisorRegister, base_name='supervisor-register')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'rest/', include(router.urls)),
    # url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^foo/', foo_view),
    url(r'^f/auth', memviews.login),
    url(r'^f/createcomment', progviews.create_comment),
    url(r'^f/creatework', progviews.create_work),
    url(r'^f/deletecomment', progviews.delete_comment),
    url(r'^f/download', appview.download_file),
    url(r'^f/getallfield', appview.get_all_expertise),
    url(r'^f/getgraduated', memviews.graduated_student),
    url(r'^f/gettask', progviews.get_task),
    url(r'^f/getungraduated', memviews.ungraduated_student),
    url(r'^f/getusername', memviews.get_username),
    url(r'^f/isexist', memviews.is_username_exist),
    url(r'^f/resetpassword', memviews.reset_password),
    url(r'^f/search', memviews.search_by_expertise),
    url(r'^f/searchfield', appview.search_expertise),
    url(r'^g/getlistthesis', appview.get_thesis_list),
    # url(r'^g/app', appview.register_app),
    url(r'^s/claim', progviews.submit_final),
    url(r'^s/editprofil', memviews.student_profile),
    url(r'^s/get', memviews.get_student),
    url(r'^s/getall', memviews.get_all_students),
    url(r'^s/inputcode', memviews.input_code),
    url(r'^s/propose', memviews.student_propose),
    # url(r'^s/register', memviews.student_register),
    url(r'^s/savethesis', memviews.save_thesis),
    url(r'^su/addtask', progviews.add_template_task),
    url(r'^su/claim', progviews.validate_final),
    url(r'^su/createtask', progviews.create_task),
    url(r'^su/createtemplate', progviews.create_template),
    url(r'^su/deletefield', memviews.delete_expertise),
    url(r'^su/deletetask', progviews.delete_task),
    url(r'^su/deletetemplate', progviews.delete_template),
    url(r'^su/editprofil', memviews.supervisor_profile),
    url(r'^su/get', memviews.get_supervisor),
    url(r'^su/getall', memviews.get_all_supervisors),
    url(r'^su/getstudentprogress', progviews.student_progress),
    url(r'^su/issupervisor', memviews.is_student_supervisor),
    # url(r'^su/register', memviews.SupervisorRegister),
    url(r'^su/removetask', progviews.del_template_task),
    url(r'^su/response', memviews.respond_proposal),
    url(r'^su/savefield', memviews.save_expertise),
    url(r'^su/updatetask', progviews.update_task),
    url(r'^su/updatetasktemplate', progviews.edit_template_task),
    url(r'^su/updatetemplate', progviews.update_template),
    url(r'^su/validation', progviews.validate_task),
]
