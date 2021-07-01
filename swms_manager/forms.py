from django import forms
from django.forms import ModelForm
from .models import *


# class SiteForm(ModelForm):
#     class Meta:
#         model = Site
#         fields = '__all__'
#
#
# class JobForm(ModelForm):
#     class Meta:
#         model = Job
#         fields = '__all__'


class SwmsForm(ModelForm):
    class Meta:
        model = Swms
        fields = '__all__'
        widgets = {'swms_groups': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):

            if self.fields[field].__class__ == forms.fields.BooleanField:
                self.fields[field].widget.attrs.update({
                    'class': 'form-check-input'

                })
            else:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'

                })


class SwmsGroupForm(ModelForm):
    class Meta:
        model = SwmsGroupDefault
        fields = '__all__'


class JobTaskForm(ModelForm):
    class Meta:
        model = JobTaskDefault
        fields = '__all__'
