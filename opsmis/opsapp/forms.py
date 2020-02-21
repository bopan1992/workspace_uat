from django import forms

class BatchInfoForm(forms.ModelForm):
    #序号、作业、开始时间、结束时间、小计、异常情况、异常处理人员
    task_date_1 = forms.DateField(label='日前批量', widget=forms.DateInput(attrs={'type': 'time'}))
    task_date_2 = forms.DateField(label='核心换日', widget=forms.DateInput(attrs={'type': 'time'}))
    task_date_3 = forms.DateField(label='异步检查', widget=forms.DateInput(attrs={'type': 'time'}))
    task_date_4 = forms.DateField(label='批量处理', widget=forms.DateInput(attrs={'type': 'time'}))
    task_date_5 = forms.DateField(label='机构撤并', widget=forms.DateInput(attrs={'type': 'time'}))
    task_date_6 = forms.DateField(label='批后处理', widget=forms.DateInput(attrs={'type': 'time'}))
    task_date_7 = forms.DateField(label='存款批量_7_数据清理', widget=forms.DateInput(attrs={'type': 'time'}))
    task_date_8 = forms.DateField(label='会计批量', widget=forms.DateInput(attrs={'type': 'time'}))
    task_date_9 = forms.DateField(label='SP001_数据库表清理_会计_状态监控', widget=forms.DateInput(attrs={'type': 'time'}))