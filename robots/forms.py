import json

from django import forms

from .validation import validate_model
from .models import Robot


class JsonForm(forms.Form):
    json_data = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        data = json.loads(cleaned_data['json_data'])
        validate_model(data)
        return data


class RobotForm(forms.ModelForm):

    class Meta:
        model = Robot
        fields = ("model", "version", "created")

    def clean(self):
        cleaned_data = super().clean()
        validate_model(cleaned_data)
        return cleaned_data