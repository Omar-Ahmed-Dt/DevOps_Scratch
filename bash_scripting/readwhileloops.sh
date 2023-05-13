#!/bin/bash

while read line; do 
    echo "$line"
done < "$1"

echo ====================
echo

while read line; do 
    echo "$line"
done < <(ls $(pwd))
