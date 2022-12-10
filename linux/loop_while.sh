#!/bin/bash 

counter=0 

while [ $counter -lt 5 ]
do
  echo $counter
  counter=$(($counter + 1))
  sleep 2 
done 


echo "Out of The loop.."

counter=2 

while true 
do
  echo $counter
  counter=$(($counter * 2))
  sleep 1 
done 
