from django import forms
from django.utils.translation import gettext as _
from .models import Label


class LabelForm(forms.ModelForm):
    name = forms.CharField(
        label=_('Name'),
        label_suffix='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Name')
            }),
        )

    class Meta:
        model = Label
        fields = [_('name')]
