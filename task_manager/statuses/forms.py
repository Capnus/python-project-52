from django import forms
from django.utils.translation import gettext as _
from .models import Status


class StatusForm(forms.ModelForm):
    name = forms.CharField(
        label=_("Name"),
        label_suffix='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Name')
            }),
        )

    class Meta:
        model = Status
        fields = [_('name')]
