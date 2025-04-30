from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django_filters.views import FilterView
from django.utils.translation import gettext as _

from task_manager.mixins import AuthRequiredMixin, AuthorDeletionMixin
from task_manager.users.models import User
from .models import Task
from .forms import TaskForm
from .filters import TaskFilter


class TasksListView(AuthRequiredMixin, FilterView):
    '''
    Show all Tasks. User authorization is required
    '''
    template_name = 'tasks/list.html'
    model = Task
    filterset_class = TaskFilter
    context_object_name = 'tasks'
    extra_context = {
        'header': _('tasks')
    }


class TaskDetailView(AuthRequiredMixin, DetailView):
    '''
    Show Task details. User authorization is required
    '''
    template_name = 'tasks/detail.html'
    model = Task
    context_object_name = 'task'
    extra_context = {
        'header': _('Task preview')
    }


class TaskCreateView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    '''
    Create new Task. User authorization is required
    '''
    template_name = 'tasks/create.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully created')
    extra_context = {
        'header': _('Create task'),
        'button_title': _('Create'),
    }

    def form_valid(self, form):

        user = self.request.user
        form.instance.author = User.objects.get(pk=user.pk)
        return super().form_valid(form)


class TaskUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    '''
    Edit existing Task. User authorization is required
    '''
    template_name = 'tasks/create.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully updated')
    extra_context = {
        'header': _('Edit task'),
        'button_title': _('Edit'),
    }


class TaskDeleteView(AuthRequiredMixin, AuthorDeletionMixin,
                     SuccessMessageMixin, DeleteView):
    '''
    Delete existing Task. User authorization is required
    Only the author can delete his tasks.
    '''
    template_name = 'tasks/delete.html'
    model = Task
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully deleted')
    author_message = _('Only the task author can delete it')
    author_url = reverse_lazy('tasks')
    extra_context = {
        'header': _('Delete task'),
        'button_title': _('Yes, delete'),
    }
