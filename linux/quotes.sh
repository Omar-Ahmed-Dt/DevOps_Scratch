#!/bin/bash

# up=$(uptime)
up=`uptime`

echo "The Uptime is $up"
echo "The Uptime is \$up" # \ ignore the meaning of the special characters
echo 'The Uptime is $up'
