#!/bin/bash

git checkout gh-pages
git merge master
/home/makefu/repos/energydb/generate_html.py
git commit -a -m "merged in changes from master"
git push
git checkout master

