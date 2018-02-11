---
layout: post
title:  "Macbook Setup"
date:   2018-02-10 14:39:40 +0800
categories: macbook mbp journal tech setup
---

## Table of Contents

{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

## 0. Basic Setup

### Badassify your ternimal and shell [todo]

> http://jilles.me/badassify-your-terminal-and-shell


## 0.5 Setting up Github Page

### Installing and Get Started with Jekyll

> https://jekyllrb.com/docs/quickstart/
> for my infor about **kramdown**: https://github.com/blog/2100-github-pages-now-faster-and-simpler-with-jekyll-3-0

#### Requirement for Jekyll

> https://stackoverflow.com/questions/38194032/how-to-update-ruby-version-2-0-0-to-the-latest-version-in-mac-osx-yosemite
> https://rubygems.org/pages/download
> https://jekyllrb.com/docs/installation/#requirements

##### 1. Update Ruby

1. `rvm list known`
2. `rvm install ruby-2.5.0`
3. `ruby -v` will give you `ruby 2.5.0p0 (2017-12-25 revision 61468) [x86_64-darwin16]`

##### 2. Update RubyGems

1. `gem update --system`
2. `gem -v` will give you `2.7.5`


#### Install Jekyll

> https://jekyllrb.com/docs/quickstart/
> https://jekyllrb.com/docs/installation/#requirements

**`gem install jekyll bundle`**

#### Markdown Renderer [todo]

Defualt: `markdown:    kramdown`

https://kramdown.gettalong.org/converter/html.html

##### Red Carpet

> https://jekyllrb.com/docs/configuration/#markdown-options


## 0.6 Shell Text Editor [todo]

**nano, Emacs & Vim**

## I use nano for the moment..

> https://wiki.gentoo.org/wiki/Nano

It seems that using nano paste in Mac is not straightforward enough
https://apple.stackexchange.com/questions/110793/how-to-copy-and-paste-lines-in-nano-on-osx

To move the cursor to the line-start and line-end: use `control+a` and `control+e`

* line start: `^+a`
* line end: `^+e`



## 1. Make IPython console Available in Pycharm [todo]

> https://www.jetbrains.com/help/pycharm/scientific-tools.html
> http://jupyter.org/

## 2. Building my Old Django Blog in the server

**Important: the server I use to deploy is `HeroKu`**

**The Email I use to register is u0905217@gmail.com**

**I used the qudong452@gmail.com, but I forgot the pwd and now cannot log-in**


## 3. Setting Up the Virtual Environment for Python (virtualenv)

> http://django-tinymce.readthedocs.io/en/latest/installation.html#prerequisites

1. navigate to Documents/
2. in bash: type `mkdir tinymce_test`
3. `ls tinymce_test`
4. after we are in the project dir 
5. build the virtualenv in this project
6. by typing `virtualenv --no-site-packages env`
    * it will show: `Using base prefix '/usr/local/Cellar/python3/3.6.4_2/Frameworks/Python.framework/Versions/3.6'
New python executable in /Users/qudong/env/bin/python3.6
Also creating executable in /Users/qudong/env/bin/python
Installing setuptools, pip, wheel...done.`
7. 


## 4. Using the Virtualenv to Build a Django APP with tinymce