from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from opsapp.models import JobInfo, BatchInfo

admin.site.site_header = '操作管理系统'
admin.site.site_title = '平安银行科技运营中心操作管理系统'

 #导入需要管理的数据库表
#批量信息
@admin.register(BatchInfo)
class BatchInfoAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('task_date','sys_name', 'sys_desc', 'task_name', 'task_desc', 'begin_time', 'end_time',
                    'error_msg','error_user')
    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('-task_date',)
    search_fields = ('sys_name',)  # 搜索字段

#工作信息
@admin.register(JobInfo)
class JobInfoAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('job_id', 'job_time', 'job_content', 'job_type', 'apply_user', 'apply_time', 'modify_user',
                    'modify_time', 'job_status')
    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('job_id',)
    #设置哪些字段可以点击进入编辑界面
    # list_display_links = ('id', 'job_content')
    # list_per_page设置每页显示多少条记录，默认是100条
    #list_per_page = 50
    # list_editable 设置默认可编辑字段
    #list_editable = ['modify_user']
    #筛选器
    #list_filter =('trouble', 'go_time', 'act_man__user_name', 'machine_room_id__machine_room_name') #过滤器
    search_fields =('job_content',) #搜索字段
    #date_hierarchy = 'apply_time'    # 详细时间分层筛选　

    # def jobStatusTrans(self , obj):
    #     if obj.job_status == 1:
    #         return format_html('<span style="color:red">{}</span>','无效')
    #     else:
    #         return format_html('<span style="color:green">{}</span>','有效')
    # jobStatusTrans.short_description = '状态'
    #
    # def jobTypeTrans(self, obj):
    #     if obj.job_type == 1:
    #         return format_html('<span style="color:red">{}</span>','工作日')
    #     else:
    #         return format_html('<span style="color:green">{}</span>', '每日')
    # jobTypeTrans.short_description = '工作类型'

