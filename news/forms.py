from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
import re

from .models import News


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
                    label="Имя пользователя:",
                    widget=forms.TextInput(attrs={
                        "class": "form-control", "autofocus": '-1'
                    }))
    password = forms.CharField(
                    label="Пароль:",
                    widget=forms.PasswordInput(attrs={
                        "class": "form-control"
                    }))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
                    label="Имя пользователя:",
                    help_text='Name consists of 150 letters only',
                    widget=forms.TextInput(attrs={
                        "class": "form-control", "autofocus": '-1'
                    }))
    password1 = forms.CharField(
                    label="Пароль:",
                    widget=forms.PasswordInput(attrs={
                        "class": "form-control"
                    }))
    password2 = forms.CharField(
                    label="Подтверждение пароля:",
                    widget=forms.PasswordInput(attrs={
                            "class": "form-control"
                    }))
    email = forms.EmailField(
                    label="Email:",
                    widget=forms.EmailInput(attrs={
                            "class": "form-control"
                    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    #Here I override autofocus
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': False})

        # Only username is possible to edit for css
        # widgets = {
        #     'username': forms.TextInput(attrs={"class": "form-control"}),
        #     'email': forms.EmailInput(attrs={"class": "form-control"}),
        #     'password1': forms.PasswordInput(attrs={"class": "form-control"}),
        #     'password2': forms.PasswordInput(attrs={"class": "form-control"}),
        # }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'category': forms.Select(attrs={"class": "form-control"})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError(
                'Название не должно начинаться с цифры')
        return title


# Для не связанной с моделью формой
# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Название',
#                             widget=forms.TextInput(attrs={"class": "form-control"}))
#     content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(
#         attrs={"class": "form-control", "rows": 5}))
#     is_published = forms.BooleanField(
#         label='Опубликовано', initial=True)
#     category = forms.ModelChoiceField(
#         queryset=Category.objects.all(),
#         label='Категория',
#         empty_label='Выбери', widget=forms.Select(attrs={"class": "form-control"})
#     )
