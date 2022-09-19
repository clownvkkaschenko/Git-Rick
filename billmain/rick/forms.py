import re
from http import HTTPStatus

from django import forms
from django.core.validators import URLValidator

from .helpers import git_ratelimit, git_status, rick_status
from .models import Profile

url_validator = URLValidator()


class ProfileForm(forms.ModelForm):
    url_profile = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(
            attrs={'placeholder': 'https://github.com/clownvkkaschenko'})
    )

    class Meta:
        model = Profile
        fields = ['url_profile']

    def clean_url_profile(self):
        data = self.cleaned_data['url_profile']
        username = data.split('/')[-1]
        valid_url = re.match(r'https://github.com/[^\W_]+(-[^\W_]+)*$', data)

        if not data:
            raise forms.ValidationError('This field is required')
        elif rick_status() != HTTPStatus.OK:
            raise forms.ValidationError(
                'Rick and Morty API not responding right now')
        try:
            url_validator(data)
        except forms.ValidationError:
            raise forms.ValidationError('Enter a valid URL')

        if 'https://github.com/' not in data:
            raise forms.ValidationError(
                'Enter a valid URL for your GitHub profile')
        elif not valid_url:
            raise forms.ValidationError(
                'Make sure you enter the URL with the GitHub profile')
        elif git_status(username) == HTTPStatus.NOT_FOUND:
            raise forms.ValidationError('Your account was not found')
        elif git_ratelimit() < 9:
            raise forms.ValidationError(
                'API request limit exceeded')
        elif git_status(username) != HTTPStatus.OK:
            raise forms.ValidationError('GitHub not responding')
        return data
