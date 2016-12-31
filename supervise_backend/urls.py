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
router.register(r'app/appregister', appview.RegisterApp, base_name='app-register')
# router.register(r'f/auth', memviews.Login, base_name='app-login')
# router.register(r'app/members/(?P<username>.+)/$', memviews.MemberList, base_name='member-list')
# router.register(r'su/editprofil', memviews.SupervisorProfile, base_name='supervisor-edit-profile')
router.register(r'app/register', memviews.RegisterViewset, base_name='member-register')
router.register(r'students', memviews.StudentViewsets, base_name='student')
router.register(r'supervisors', memviews.SupervisorViewsets, base_name='supervisor')
router.register(r'expertises', memviews.ExpertiseViewsets, base_name='expertise')
router.register(r'theses', progviews.ThesisViewsets, base_name='thesis')
router.register(r'templates', progviews.TemplateViewsets, base_name='template')
router.register(r'tasks', progviews.StudentTaskViewsets, base_name='task')
router.register(r'users', memviews.UserViewsets, base_name='user')

urlpatterns = [    
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include('smuggler.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'', include(router.urls)),
    url(r'app/members/(?P<username>.+)/$', memviews.MemberList.as_view()),
    # url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^foo/', foo_view),
    # url(r'^f/auth', memviews.login),
]
