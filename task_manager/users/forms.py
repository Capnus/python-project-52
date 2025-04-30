from django import forms
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext as _
from .models import User


class UserForm(forms.ModelForm):

    first_name = forms.CharField(
        max_length=150,
        required=True,
        label=_("First name"),
        label_suffix='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('First name'),
            'required': True,
        })
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        label=_("Last name"),
        label_suffix='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Last_name'),
            'required': True,
        })
    )

    username = forms.CharField(
        max_length=150,
        required=True,
        label=_("Username"),
        label_suffix='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Username'),
            'required': True,
        }),
        help_text=_("Required field. No more than 150 characters. Only letters, numbers and symbols @/./+/-/_.")  # noqa: E501
    )

    password1 = forms.CharField(
        label=_("Password"),
        label_suffix='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Password'),
            'required': True,
        }),
        help_text=_("Your password must be at least 3 characters long.")
    )

    password2 = forms.CharField(
        label=_("Password confirmation"),
        label_suffix='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Password confirmation'),
            'required': True,
        }),
        help_text=_("To confirm, please enter your password again.")
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        )

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exclude(id=self.instance.id).exists():  # noqa: E501
            raise forms.ValidationError(_('A user with this name already exists.'))  # noqa: E501
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password2', _('The passwords do not match.'))

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        password = self.cleaned_data.get('password1')
        if password:
            user.password = make_password(password)

        if commit:
            user.save()

        return user
