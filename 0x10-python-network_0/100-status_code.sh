#!/bin/bash
# sends a req to $1 URL, display response status code only
awk 'NR==1{printf "%s", $2}' test7 $(curl -sI "$1" -o test7)
