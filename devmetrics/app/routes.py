from flask import Blueprint, render_template, redirect, url_for
from flask_dance.contrib.github import github


main = Blueprint('main', __name__)

@main.route('/')
def index():
    if not github.authorized:
        return redirect(url_for('github.login'))
    resp= github.get('/user')
    assert resp.ok, resp.text
    github_info = resp.json()
    username = github_info['login']

    repos_resp = github.get('/user/repos')
    repos = repos_resp.json() if repos_resp.ok else []

    return render_template('index.html', username=username, repos=repos)
