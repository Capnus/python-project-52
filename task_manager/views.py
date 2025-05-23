from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.translation import gettext as _


class IndexView(TemplateView):
    template_name = 'index.html'


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('home')
    success_message = _("You logged in")

    def form_invalid(self, form):
        return super().form_invalid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    success_message = _('You logged out')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You logged out'))
        return super().dispatch(request, *args, **kwargs)
