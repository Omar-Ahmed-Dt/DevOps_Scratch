#!/bin/bash

# for i in python java ruby c# c golang 
# do
#   echo "Looping .... "
#   sleep 3
#   echo $i 
#   echo "#############"
# done 


# Show files for the same directory ;
#for i in $ls
### OR 
for i in `ls` 
do 
  echo "Looping ..."
  echo $i 
  sleep 2 

done 

