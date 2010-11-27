#!/bin/bash
IPATH='/home/makefu/repos/energydb/drinks/img/'
if [ -z "$1" ] || [ -z "$2" ];then
  echo "usage add_drink IMAGE DRINK_KEY"
  exit -1
fi
#TODO fix the absolute path stuff
convert -resize x600 "$1" $IPATH"$2".jpg
convert -resize x100 "$1" $IPATH"thumb_"$2.jpg
