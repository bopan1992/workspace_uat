from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# def hello(request):
#     return HttpResponse('hello，欢迎使用Django！By bopan')

def reportdplus(request):
    return render(request, 'opsapp/report/reportdplus.html')

def reportmurex(request):
    return render(request, 'opsapp/report/reportmurex.html')

def reportdemo(request):
    return render(request, 'opsapp/report/reportdemo.html')

def operaduty(request):
    return render(request, 'opsapp/duty/operaduty.html')

def opsduty(request):
    return render(request, 'opsapp/duty/opsduty.html')

def index(request):
    sitename = 'Django中文网'
    url = 'www.django.cn'
    #新加一个列表
    list=[
        '开发前的准备',
        '项目需求分析',
        '数据库设计分析',
        '创建项目',
        '基础配置',
        '欢迎页面',
        '创建数据库模型',
    ]
    #在来的基础上新加一个字典
    mydict={
        'name': '吴秀峰',
        'qq': '445813',
        'wx': 'vipdjango',
        'email': '445813@qq.com',
        'Q群': '10218442',
    }
    context = {
        'sitename': sitename,
        'url':url,
        'list':list, #把list封装到context
        'mydict': mydict,# 把mydict封装到上下文
    }
    return render(request, 'opsapp/index.html', context)

