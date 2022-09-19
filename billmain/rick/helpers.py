import time
from random import randint

import requests

HEAD = {'Authorization': 'token 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'}


def rick_status():
    """Checking Rick and Morty API Status"""
    url = 'https://rickandmortyapi.com/api/character'
    return requests.get(url).status_code


def git_status(username):
    """Checking GitGub API Status"""
    url = f'https://api.github.com/users/{username}'
    return requests.get(url, headers=HEAD).status_code


def git_ratelimit():
    """Show request limit"""
    url = 'https://api.github.com'
    return int(
        requests.get(url, headers=HEAD).headers['X-RateLimit-Remaining'])


def rick_content():
    """Getting the necessary content about a random character"""
    info = {}
    page, character = randint(1, 41), randint(0, 19)
    contents = ['name', 'image', 'species', 'status', 'location', 'episode']
    url = f'https://rickandmortyapi.com/api/character?page={page}'

    resp = requests.get(url).json()['results'][character]
    for content in contents:
        response = resp.get(content)
        if content == 'location':
            info[content] = response.get('name')
        elif content == 'episode':
            info[content] = requests.get(response[0]).json().get('name')
        else:
            info[content] = response
    return info


def github_content(username):
    """Getting the required content about the selected profile"""
    info = {}
    contents = ['id', 'avatar_url', 'name', 'public_repos']
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url, headers=HEAD).json()

    for content in contents:
        info[content] = response.get(content)
    return info


def git_followers(username):
    """Find out the number of followers to the selected profile"""
    url = f'https://api.github.com/users/{username}/followers'
    try:  # if there are two or more pages with repositories
        link = requests.get(url, headers=HEAD).headers['Link']
        shear = link.split('page=')[-1]
        last_page = int(shear.split(r'>')[0])
        followers = (last_page - 1) * 30
        url = (f'https://api.github.com/users/{username}/'
               f'followers?page={last_page}')
        followers += len(requests.get(url, headers=HEAD).json())
        return followers
    except KeyError:  # if only one page with repositories
        return len(requests.get(url, headers=HEAD).json())


def git_repos(username):
    """Get the name and url of the repository"""
    url = f'https://api.github.com/users/{username}/repos?sort=pushed'
    response = requests.get(url, headers=HEAD).json()
    repos = {}
    for i in range(3):
        try:
            name = response[i].get('name')
            urls = response[i].get('svn_url')
        except IndexError:
            break
        repos[name] = urls
    return repos


def latest_programming_language(username):
    """Returns the latest programming language"""
    url = f'https://api.github.com/users/{username}/repos?sort=pushed'
    response = requests.get(url, headers=HEAD).json()
    cnt_repos = len(response)
    if cnt_repos == 0:
        return None
    language = response[0].get('language')
    return language


def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format)
        time.sleep(1)
        num_of_secs -= 1
