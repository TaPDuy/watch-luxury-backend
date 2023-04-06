#!/bin/bash

absdir=$(realpath "$( dirname "$0" )")
if [ $# -eq 0 ]
then
    "$absdir"/../.venv/bin/python "$absdir"/../manage.py test
else
    "$absdir"/../.venv/bin/python "$absdir"/../manage.py test "$*"
fi
