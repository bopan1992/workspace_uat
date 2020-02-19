from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html

from DjangoUeditor.models import UEditorField

# 导入Django自带用户模块
#批量信息
class BatchInfo(models.Model):
    models.AutoField
    sys_name_choices = (
        ('Dplus', 'Dplus'),
        ('Murex', 'Murex'),
        ('FBS', 'FBS'),
    )
    sys_name = models.CharField('系统名称', choices=sys_name_choices, max_length=20)
    sys_desc = models.CharField('系统描述', max_length=20)
    task_name = models.CharField('任务名称', max_length=20)
    task_desc = models.CharField('任务描述', max_length=20)
    task_date = models.DateField('批量日期')
    begin_time =  models.DateTimeField('开始时间')
    end_time = models.DateTimeField('结束时间')
    error_msg = models.CharField('异常情况', max_length=50, default='')
    error_user = models.CharField('异常处理人', max_length=20, default='')

    class Meta:
        verbose_name = '作业信息'
        verbose_name_plural = verbose_name

#工作信息
class JobInfo(models.Model):
    #id = models.CharField('ID', max_length=20, primary_key=True)
    models.AutoField
    job_id = models.IntegerField('工作序号', default='')
    job_time = models.CharField('时间', max_length=10, default='')
    job_content = models.CharField('工作内容', max_length=100, default='')
    type_choices = (
        (0, '未知'),
        (1, '工作日'),
        (2, '每天'),
    )
    job_type = models.IntegerField('工作类型', choices=type_choices, default=2)
    apply_user = models.CharField('创建人', max_length=10, default='')
    apply_time = models.DateTimeField('创建时间', auto_now_add=True)
    modify_user = models.CharField('修改人', max_length=10, default='')
    modify_time = models.DateTimeField('修改时间', auto_now=True)
    status_choices = (
        (0, '未知'),
        (1, '有效'),
        (2, '无效'),
    )
    job_status = models.IntegerField('状态', choices=status_choices, default=1)

    class Meta:
        verbose_name = '工作信息'
        verbose_name_plural = verbose_name

