#!/bin/bash

git checkout gh-pages
git merge master
CURR=`pwd`
cd /home/makefu/repos/energydb
./generate_html.py
cd $CURR
git commit -a -m "merged in changes from master"
git push
git checkout master

