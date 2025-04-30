from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from task_manager.mixins import AuthRequiredMixin, DeleteProtectionMixin
from .models import Label
from .forms import LabelForm


class LabelsListView(AuthRequiredMixin, ListView):
    '''
    Show all Labels. User authorization is required
    '''
    template_name = 'labels/list.html'
    model = Label
    context_object_name = 'labels'
    extra_context = {
        'header': _('Labels')
    }


class LabelCreateView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    '''
    Create new Label. User authorization is required
    '''
    template_name = 'labels/create.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully created')
    extra_context = {
        'header': _('Create label'),
        'button_title': _('Create')
    }


class LabelUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    '''
    Edit existing Label. User authorization is required
    '''
    template_name = 'labels/create.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully updated')
    extra_context = {
        'header': _('Edit label'),
        'button_title': _('Edit')
    }


class LabelDeleteView(AuthRequiredMixin, DeleteProtectionMixin,
                      SuccessMessageMixin, DeleteView):
    '''
    Delete existing Label. User authorization is required
    If the label is associated with at least one task it cannot be deleted.
    '''
    template_name = 'labels/delete.html'
    model = Label
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully deleted')
    protected_message = _("Unable to delete label, it is in use")
    protected_url = reverse_lazy('labels')
    extra_context = {
        'header': _('Delete label'),
        'button_title': _('Yes, delete')
    }
