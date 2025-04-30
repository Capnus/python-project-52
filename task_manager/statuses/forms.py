from django import forms
from .models import Status


class StatusForm(forms.ModelForm):
    name = forms.CharField(
        label="Name",
        label_suffix='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name'
            }),
        )

    class Meta:
        model = Status
        fields = ['name']
