from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# def hello(request):
#     return HttpResponse('hello，欢迎使用Django！By bopan')
def turnoverlive(request):
    return render(request, 'opsapp/opslive/turnoverlive.html')

def systemlive(request):
    return render(request, 'opsapp/opslive/systemlive.html')

def commandlive(request):
    return render(request, 'opsapp/opslive/commandlive.html')

def batchrunlive(request):
    return render(request, 'opsapp/opslive/batchrunlive.html')

def importdplus(request):
    return render(request, 'opsapp/work/importdplus.html')

def importmurex(request):
    return render(request, 'opsapp/work/importmurex.html')

def operlog(request):
    return render(request, 'opsapp/work/operlog.html')

def dplusreport(request):
    return render(request, 'opsapp/report/dplusreport.html')

def murexreport(request):
    return render(request, 'opsapp/report/murexreport.html')

def majortask(request):
    return render(request, 'opsapp/report/majortask.html')

def majorreport(request):
    return render(request, 'opsapp/report/majorreport.html')

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

