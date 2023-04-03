from django import forms
from .models import Record


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['name',"age", 'gender', 'salary']

    def __init__(self,*args,**kwargs):
        super(RecordForm, self).__init__(*args,**kwargs)
    #     self.fields['name'].widget.attrs['placeholder'] = 'Your name'
    #     self.fields['age'].widget.attrs['placeholder'] = 'Your age'
        self.fields['gender'].label = 'Check if Male'
    #     self.fields['salary'].widget.attrs['placeholder'] = 'Your income'

    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class'] = 'form-control'
