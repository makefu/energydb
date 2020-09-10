#!/bin/bash
set -euf
HERE=$(dirname "$(readlink -f "$0")")
IPATH="$HERE/../drinks/img/"
if [ -z "${1:-}" ];then
  echo "usage add_drink IMAGE"
  exit -1
fi
img=${1%.*}
convert -resize x600 "$1" "$IPATH/${img}.jpg"
convert -resize x100 "$1" "$IPATH/thumb_${img}.jpg"
