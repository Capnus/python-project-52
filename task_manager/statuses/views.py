from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _

from task_manager.mixins import AuthRequiredMixin, DeleteProtectionMixin
from .models import Status
from .forms import StatusForm


class StatusesListView(AuthRequiredMixin, ListView):
    '''
    Show all Statuses. User authorization is required
    '''
    template_name = 'statuses/list.html'
    model = Status
    context_object_name = 'statuses'
    extra_context = {
        'header': _('Statuses')
    }


class StatusCreateView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    '''
    Create new Status. User authorization is required
    '''
    template_name = 'statuses/create.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully created')
    extra_context = {
        'header': _('Create status'),
        'button_title': _('Create'),
    }


class StatusUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    '''
    Edit existing Status. User authorization is required
    '''
    template_name = 'statuses/create.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully updated')
    extra_context = {
        'header': _('Edit status'),
        'button_title': _('Edit'),
    }


class StatusDeleteView(AuthRequiredMixin, DeleteProtectionMixin,
                       SuccessMessageMixin, DeleteView):
    '''
    Delete existing Status. User authorization is required
    If the status is associated with at least one task it cannot be deleted.
    '''
    template_name = 'statuses/delete.html'
    model = Status
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully deleted')
    protected_message = _('Unable to delete status, it is in use')
    protected_url = reverse_lazy('statuses')
    extra_context = {
        'header': _('Delete status'),
        'button_title': _('Yes, delete')
    }
