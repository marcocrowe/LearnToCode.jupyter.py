#!/usr/bin/env python
# coding: utf-8

# # Set all filenames to lowercase

# <!--
# import data_analytics.github as github
# print(github.create_jupyter_notebook_header("markcrowe-com", "LearnToCode.jupyter.py", "topic-09-02-set-all-file-names-to-lower-case/set-all-file-names-to-lower-case.ipynb", "master"))
# -->
# <table style="margin: auto;"><tr><td><a href="https://mybinder.org/v2/gh/markcrowe-com/LearnToCode.jupyter.py/master?filepath=topic-09-02-set-all-file-names-to-lower-case/set-all-file-names-to-lower-case.ipynb" target="_parent"><img src="https://mybinder.org/badge_logo.svg" alt="Open In Binder"/></a></td><td>online editors</td><td><a href="https://colab.research.google.com/github/markcrowe-com/LearnToCode.jupyter.py/blob/master/topic-09-02-set-all-file-names-to-lower-case/set-all-file-names-to-lower-case.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td></tr></table>

# ## Objective

# The objective is to set all filenames of the sub files/directories of a directory to lowercase.

# ## Setup
# Import required Python packages.

# ### Command Readme

# #### Online install packages command
# 
# ```python
# !pip install -r https://raw.githubusercontent.com/markcrowe-com/LearnToCode.jupyter.py/master/topic-09-02-set-all-file-names-to-lower-case/requirements.txt --quiet
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

# ## Imports

import os


# ## User input

path: str = input("Enter folder:")


# ## Set all filenames of the sub files/directories of a directory to lowercase.

def rename_file_system_object(parent_directory, file_name):
    new_file_name: str = file_name.lower()
    if (file_name != new_file_name):
        print(f"Renaming:'{file_name}' to '{new_file_name}'")
        os.rename(os.path.join(parent_directory, file_name),
                  os.path.join(parent_directory, new_file_name))


print(path)
print()
for parent_directory, directories, filenames in os.walk(path):
    for file_name in filenames:
        rename_file_system_object(parent_directory, file_name)
    for directory_name in directories:
        rename_file_system_object(parent_directory, directory_name)


# Author &copy; 2022 <a href="https://github.com/markcrowe-com" target="_parent">Mark Crowe</a>. All rights reserved.
