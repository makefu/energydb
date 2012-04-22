#!/bin/bash
IPATH='/home/makefu/repos/energydb/drinks/img/'
if [ -z "$1" ];then
  echo "usage add_drink IMAGE"
  exit -1
fi
img=${1%.*}
#TODO fix the absolute path stuff
convert -resize x600 "$1" $IPATH"$img".jpg
convert -resize x100 "$1" $IPATH"thumb_"$img.jpg
