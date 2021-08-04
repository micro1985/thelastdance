#!/bin/bash

FILE=$1

if [ -f "$FILE" ]; then
  if grep "Hostname" $FILE; then
    echo "File exist && norm"
    exit 0
  fi
fi

exit 1
