'''
 _   _  _______   _______   _____  
| \ | ||  ___\ \ / /_   _| |  ___| 
|  \| || |__  \ V /  | |   | |__   
| . ` ||  __| /   \  | |   |  __|  
| |\  || |___/ /^\ \ | |   | |___  
\_| \_/\____/\/   \/ \_/   \____/  

Author: ziyu (Chen Zhaoyu)
Date: 2025-10-05 14:28:16
LastEditors: ziyu (Chen Zhaoyu)
LastEditTime: 2025-10-05 17:16:51
Description: 
Copyright (c) 2025 by XAUT NEXT-E/ziyu, All Rights Reserved. 
'''

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ne_vision'
copyright = '2025, XAUT NEXT-E Robotics Team'
author = 'XAUT NEXT-E Robotics Team'
release = 'dev'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark',
    'sphinx_markdown_tables'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'zh-CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
