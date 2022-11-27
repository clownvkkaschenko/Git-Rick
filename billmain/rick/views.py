from django.shortcuts import redirect, render

from .forms import ProfileForm
from .helpers import (git_followers, git_ratelimit, git_repos, github_content,
                      programming_language, rick_content)
from .models import Profile


def index(request):
    if request.method != 'POST':
        form = ProfileForm()
        limit = git_ratelimit
        context = {
            'form': form,
            'limit': limit
        }
        return render(request, 'rick/index.html', context)
    form = ProfileForm(request.POST)
    if not form.is_valid() and git_ratelimit() <= 7:
        limit = git_ratelimit
        context = {
            'form': form,
            'limit': limit
        }
        return render(request, 'rick/index.html', context)
    elif not form.is_valid():
        return render(request, 'rick/index.html', {'form': form})
    new_url_profile = form.cleaned_data.get('url_profile')
    if not Profile.objects.filter(url_profile=new_url_profile):
        profile = form.save(commit=False)
        profile.url_profile = form.cleaned_data.get('url_profile')
        profile.rick_name = rick_content()['name']
        profile.rick_image = rick_content()['image']
        profile.rick_species = rick_content()['species']
        profile.rick_status = rick_content()['status']
        profile.rick_location = rick_content()['location']
        profile.rick_first_episode = rick_content()['episode']
        profile.save()
    request.session['url_profile'] = new_url_profile
    request.session.set_expiry(0)
    return redirect('rick:profile')


def profile(request):
    domain = request.session.get('url_profile')
    if not domain:
        return redirect('rick:index')
    username = domain.split('/')[-1]
    profile = Profile.objects.get(url_profile=domain)
    rick = {
        "name": profile.rick_name,
        "image": profile.rick_image,
        "species": profile.rick_species,
        "status": profile.rick_status,
        "location": profile.rick_location,
        "episode": profile.rick_first_episode
    }
    data = {
        "info": github_content(username),
        "followers": git_followers(username),
        "language": programming_language(username),
        "repos": list(git_repos(username).keys()),
        "url_rep": list(git_repos(username).values()),
    }
    context = {
        'rick': rick,
        'data': data,
        'domain': domain,
        'username': username
    }
    if git_ratelimit() <= 7:
        return redirect('rick:index')
    return render(request, 'rick/profile.html', context)
