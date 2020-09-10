#!/bin/sh
set -euf

cd "$(dirname "$(readlink -f "$0")")"/.. || exit 1
git checkout gh-pages
git merge master
CURR=`pwd`
echo "generating html"
./generate_html.py
git add .
git commit -a -m "merged in changes from master"
git push
git checkout master

