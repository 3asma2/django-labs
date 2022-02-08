from django import forms
from trainee.models import Trainee

class AddTraineeModelForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = ["name"]
