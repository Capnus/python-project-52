from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from task_manager.mixins import (
    AuthRequiredMixin,
    UserPermissionMixin,
    DeleteProtectionMixin,
)
from .models import User
from .forms import UserForm


class UsersListView(ListView):
    '''
    Show all Users
    '''
    template_name = 'users/list.html'
    model = User
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    """
    Create new User
    """
    template_name = 'users/create.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')
    extra_context = {
        'header': 'Registration',
        'button_title': 'Register',
    }
    success_message = 'User successfully registered'


class UserUpdateView(AuthRequiredMixin, UserPermissionMixin,
                     SuccessMessageMixin, UpdateView):
    '''
    Edit existing User. User authorization is required
    User can only edit himself
    '''
    template_name = 'users/create.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users')
    success_message = 'User successfully updated'
    permission_message = 'You do not have permission to edit another user.'
    permission_url = reverse_lazy('users')
    extra_context = {
        'header': 'Edit user',
        'button_title': 'Edit',
    }


class UserDeleteView(AuthRequiredMixin, UserPermissionMixin,
                     DeleteProtectionMixin, SuccessMessageMixin, DeleteView):
    '''
    Delete existing User. User authorization is required
    User can only delete himself
    User cannot be deleted if associated with a task
    '''
    template_name = 'users/delete.html'
    model = User
    success_url = reverse_lazy('users')
    success_message = 'User successfully deleted'
    permission_message = 'You do not have permission to edit another user.'
    permission_url = reverse_lazy('users')
    protected_message = 'Unable to delete the user.'
    protected_url = reverse_lazy('users')
