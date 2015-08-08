# coding: utf-8
from django import forms
from users.models import User
from django.utils.translation import ugettext_lazy as _


class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(
        label=_(u'Password'),
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label=_(u'Password confirm'),
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ['login', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password doesn't match!")
        return password2

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'third_name']