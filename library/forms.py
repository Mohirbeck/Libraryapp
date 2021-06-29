from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.forms.widgets import RadioSelect
from .models import Book
from django import forms
from django.core.validators import MinLengthValidator


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    group = forms.CharField(max_length=31)
    faculty = forms.CharField(max_length=63)
    username = forms.CharField(max_length=63)
    pwd1 = forms.CharField(max_length=127,
                           required=True,
                           widget=forms.PasswordInput,
                           validators=[MinLengthValidator(8)],
                           label="Password")
    pwd2 = forms.CharField(max_length=127,
                           required=True,
                           widget=forms.PasswordInput,
                           validators=[MinLengthValidator(8)],
                           label="Confirm Password")

    def clean_pwd2(self):
        if self.cleaned_data['pwd1'] != self.cleaned_data['pwd2']:
            raise ValidationError('Passwords must be the same!')

        else:

            SpecialSym = ['$', '@', '#', '%', '/']

            if len(self.cleaned_data['pwd2']) < 8:
                raise ValidationError('length should be at least 8')

            else:

                if not any(char.isdigit() for char in self.cleaned_data['pwd2']):
                    raise ValidationError(
                        'Password should have at least one numeral')

                else:

                    if not any(char.isupper() for char in self.cleaned_data['pwd2']):
                        raise ValidationError(
                            'Password should have at least one uppercase letter')

                    else:

                        if not any(char.islower() for char in self.cleaned_data['pwd2']):
                            raise ValidationError(
                                'Password should have at least one lowercase letter')

                        else:

                            if not any(char in SpecialSym for char in self.cleaned_data['pwd2']):
                                raise ValidationError(
                                    'Password should have at least one of the symbols $@#')


        return self.cleaned_data['pwd2']
