#!/bin/bash

if ! $(git diff-index --quiet HEAD);
then
  echo "still have dirty tree?"
  exit 1
fi
git checkout gh-pages
git merge master
CURR=`pwd`
cd /home/makefu/repos/energydb
./generate_html.py
git add .
cd $CURR
git commit -a -m "merged in changes from master"
git push
git checkout master

