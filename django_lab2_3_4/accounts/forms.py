from django import forms
from accounts.models import Acc


class AddStudentForm(forms.Form):
    name = forms.CharField(label="User Name", max_length=40,widget=forms.TextInput(attrs={'class': 'form-control'}))


class AddStudentModelForm(forms.ModelForm):
    class Meta:
        model = Acc
        fields = "__all__"
        labels = {
            "name": "Student Name Model Form"
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
