# Generated by Django 3.0.3 on 2020-02-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.IntegerField(default='', verbose_name='工作序号')),
                ('job_time', models.CharField(default='', max_length=10, verbose_name='时间')),
                ('job_content', models.CharField(default='', max_length=100, verbose_name='工作内容')),
                ('job_type', models.IntegerField(default='', verbose_name='工作类型')),
                ('apply_user', models.CharField(default='', max_length=10, verbose_name='创建人')),
                ('apply_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modify_user', models.CharField(default='', max_length=10, verbose_name='修改人')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('job_status', models.IntegerField(default='1', verbose_name='状态')),
            ],
            options={
                'verbose_name': '工作信息',
                'verbose_name_plural': '工作信息',
            },
        ),
    ]