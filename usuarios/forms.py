# coding=UTF-8
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django import forms
from datetime import date, datetime, timedelta
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from collections import OrderedDict

class LoginForm(AuthenticationForm):
    
    ayudas = {
              'username':u'Ingresa el nombre de tu empresa o el tuyo propio si ofreces un servicio particular.',
              'email':u'Ingresa una direcci\xf3n, si corresponde.',
              'password1':u'Escribe un buen password.',
              'password2':u'Ahora repitelo, para verificar.'
    }    

    username = forms.CharField(label=_(u'Usuario'), max_length=30, 
                                widget=forms.TextInput(
                                attrs={'class':'input-text', 'placeholder':'Nombre de usuario…'}), 
                                help_text = ayudas['username'])
    password1 = forms.CharField(label=_("Password"), 
                                widget=forms.PasswordInput(
                                attrs={'class':'input-text', 'placeholder':'Contraseña'}), 
                                   help_text=ayudas['password1'])
    class Meta:
        model = User
        fields = ("username", "password1")


class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set his/her password without entering the
    old password
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    new_password1 = forms.CharField(label=_("New password"),
                                    widget=forms.PasswordInput(attrs={'class':'form-control',
                                      'placeholder':'Contraseña'}))
    new_password2 = forms.CharField(label=_("New password confirmation"),
                                    widget=forms.PasswordInput(attrs={'class':'form-control',
                                      'placeholder':'Confirmar Contraseña'}))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user


class PasswordChangeForm(SetPasswordForm):
    """
    A form that lets a user change his/her password by entering
    their old password.
    """
    error_messages = dict(SetPasswordForm.error_messages, **{
        'password_incorrect': _("Your old password was entered incorrectly. "
                                "Please enter it again."),
    })
    old_password = forms.CharField(label=_("Old password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control',
                                      'placeholder':'Antigua Contraseña'}))

    def clean_old_password(self):
        """
        Validates that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password

PasswordChangeForm.base_fields = OrderedDict(
    (k, PasswordChangeForm.base_fields[k])
    for k in ['old_password', 'new_password1', 'new_password2']
)        