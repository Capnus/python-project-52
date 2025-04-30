from django import forms

from .models import Task
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.labels.models import Label


class TaskForm(forms.ModelForm):
    name = forms.CharField(
        label=_("Name"),
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Name'),
            }(
        )
    ))

    description = forms.CharField(
        label=_("Description"),
        label_suffix='',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': _('Description'),
            }
        )
    )

    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        label=_("Status"),
        label_suffix='',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )

    executor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label=_("Performer"),
        label_suffix='',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )

    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        label=_("Tags"),
        label_suffix='',
        required=False,
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = Task
        fields = (
            'name',
            'description',
            'status',
            'executor',
            'labels'
        )
