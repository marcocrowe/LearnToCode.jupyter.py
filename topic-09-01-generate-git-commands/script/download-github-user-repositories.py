#!/usr/bin/env python
# coding: utf-8

# # Download GitHub user repositories

# <!--
# #!pip install markcrowe
# import data_analytics.github as github
# print(github.create_jupyter_notebook_header("markcrowe-com", "LearnToCode.jupyter.py", "topic-09-01-generate-git-commands/download-github-user-repositories.ipynb", "master"))
# -->
# <table style="margin: auto;"><tr><td><a href="https://mybinder.org/v2/gh/markcrowe-com/LearnToCode.jupyter.py/master?filepath=topic-09-01-generate-git-commands/download-github-user-repositories.ipynb" target="_parent"><img src="https://mybinder.org/badge_logo.svg" alt="Open In Binder"/></a></td><td>online editors</td><td><a href="https://colab.research.google.com/github/markcrowe-com/LearnToCode.jupyter.py/blob/master/topic-09-01-generate-git-commands/download-github-user-repositories.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td></tr></table>

# ## Objective

# The objective is to generate the Git commands to clone all the repositories of a user or organization.

# ## Setup
# Import required Python packages.

# ### automate install packages code

from ipywidgets import Button, Output, RadioButtons, VBox

def display_requirements_install(url, file="requirements.txt"):
    def on_button_clicked(button):
        requirements_file: str = file if source_radio_buttons.value == 'local' else url
        with output:
            output.clear_output()
            print(f"!pip install -r {requirements_file} --quiet\n")
            #!pip install -r $requirements_file --quiet
            print("Packages installed")

    button = Button(description="Install packages")
    button.on_click(on_button_clicked)
    output = Output()
    source_radio_buttons = RadioButtons(description='Source:', options=['local', 'remote'], value='remote')
    return VBox([source_radio_buttons, button, output])


# ### Command Readme

# #### Online install packages command
# 
# ```python
# !pip install -r https://raw.githubusercontent.com/markcrowe-com/LearnToCode.jupyter.py/master/topic-09-01-generate-git-commands/requirements.txt --quiet
# ```
# 
# #### Off-line install packages command
# 
# ```python
# !pip install -r requirements.txt --quiet
# ```
# 
# #### Package for creating requirements 
# 
# ```python
# !pip install pipreqs
# ```
# 
# #### Package to recreate  requirements
# 
# ```python
# !pipreqs --force
# ```

# ### automate install packages 

url: str = "https://raw.githubusercontent.com/markcrowe-com/LearnToCode.jupyter.py/master/topic-09-01-generate-git-commands/requirements.txt"
display_requirements_install(url)


# ## Imports

from humanize import naturalsize
from IPython.display import HTML, Markdown
from math import ceil
import requests


REPOSITORY_PAGE_COUNT: int = 30


# ## User input

username: str = input()
user_api_url: str = f"https://api.github.com/users/{username}"
repositories_api_url: str = f"https://api.github.com/users/{username}/repos"


# ## Download JSON

with requests.get(user_api_url) as response:
    user_json: dict = response.json()


repository_pages = ceil(user_json["public_repos"] / REPOSITORY_PAGE_COUNT)


repositories_json: list = []
for page_number in range(1, repository_pages + 1):
    url:str = f"{repositories_api_url}?page={page_number}"
    print(url)
    with requests.get(url) as response:
        repositories_json += response.json()


# ## Generate Git commands from JSON

user_repositories_kb_size: int = 0
user_repositories_count: int = len(repositories_json)
text: str = ""
for repository_json in repositories_json:
    text += f"git clone {repository_json['clone_url']} -v\n"
    user_repositories_kb_size += int(repository_json['size'])
text = text.strip()


print(f"Total file size of {user_repositories_count} repositories is {naturalsize(user_repositories_kb_size*1_024)}\n")


display(HTML(f'<button style="float: right;" onclick="navigator.clipboard.writeText(`{text}`)">Copy</button>'))
print(text)


# Author &copy; 2022 <a href="https://github.com/markcrowe-com" target="_parent">Mark Crowe</a>. All rights reserved.
