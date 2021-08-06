#!/bin/bash

res=`python ./test.py`

if [ "$res" == "Good" ]; then
  echo "Very Good"
  exit 0
else
  echo "Very Bads756756675"
  exit 1
fi
