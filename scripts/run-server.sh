#!/bin/bash
absdir=$(realpath $( dirname $0 ))
$absdir/../.venv/bin/python $absdir/../manage.py runserver 0.0.0.0:8000
