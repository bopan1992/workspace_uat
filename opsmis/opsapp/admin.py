from django.contrib import admin

from django.http import HttpResponseRedirect

from opsapp.models import JobInfo, BatchInfo

admin.site.site_header = '操作管理系统'
admin.site.site_title = '平安银行科技运营中心操作管理系统'

#导入需要管理的数据库表
#批量信息
@admin.register(BatchInfo)
class BatchInfoAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('task_date','sys_name', 'task_name', 'begin_time', 'end_time',
                    'error_msg','error_user')
    #ordering设置默认排序字段，负号表示降序排序
    list_per_page = 10
    #自定义Action
    def import_dplus(self, request, queryset):
        pass
    import_dplus.short_description = ' D+'
    import_dplus.icon = 'fas fa-edit'
    import_dplus.style = 'color:black;'
    import_dplus.type = 'info'
    import_dplus.action_type = 1 #0=当前页内打开，1=新tab打开，2=浏览器tab打开
    import_dplus.action_url = '../importdplus'
    def import_murex(self, request, queryset):
        pass
    import_murex.short_description = ' Murex'
    import_murex.icon = 'fas fa-edit'
    import_murex.style = 'color:black;'
    import_murex.type = 'info'
    import_murex.action_type = 1 #0=当前页内打开，1=新tab打开，2=浏览器tab打开
    import_murex.action_url = '../importmurex'
    actions = ['import_dplus','import_murex']
    #Action权限管理
    # import_dplusallowed_permissions = ('change',)

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

