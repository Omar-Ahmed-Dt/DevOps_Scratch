#!/bin/bash 

free_memory=$(free -m | grep Mem | awk '{print $4}')
echo "Free Memory is $free_memory Mb"

### OR  using back ticks >>  ``

echo "########"

memory=`free -m | grep Mem | awk '{print $4}'`
echo "Free Memory is $memory Mb"

