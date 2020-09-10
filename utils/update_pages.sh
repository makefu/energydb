#!/bin/bash

if ! $(git diff-index --quiet HEAD);
then
  echo "still have dirty tree?"
  exit 1
fi
git checkout gh-pages
git merge master
CURR=`pwd`
cd "$(dirname "$(readlink -f "$0")")"/.. || exit 1
./generate_html.py
git add .
git commit -a -m "merged in changes from master"
git push
git checkout master

