"""opsmis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from opsapp import views         #+
from django.views.static import serve
#导入静态文件模块
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),   # 里面留空，代表首页
    path('ueditor/', include('DjangoUeditor.urls')), #添加DjangoUeditor的URL
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),#增加此行
    path('dplusreport/', views.dplusreport),  # dplusreport
    path('murexreport/', views.murexreport),  # murexreport
    path('majortask/', views.majortask),  # dplusreport
    path('majorreport/', views.majorreport),  # murexreport
    path('reportdemo/', views.reportdemo),  # reportdemo
    path('operaduty/', views.operaduty),  # operaduty
    path('opsduty/', views.opsduty),  # opsduty
    path('importdplus/', views.importdplus),  # work
    path('importmurex/', views.importmurex),  # work
    path('operlog/', views.operlog),
    path('turnoverlive/', views.turnoverlive),
    path('systemlive/', views.systemlive),
    path('commandlive/', views.commandlive),
    path('batchrunlive/', views.batchrunlive),
]