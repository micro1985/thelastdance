#!/bin/bash

res=`python ./test.py`

if [ "$res" == "Good" ]; then
  echo "Very Good"
  exit 0
else
  echo "Very Badsdf"
  exit 1
fi
