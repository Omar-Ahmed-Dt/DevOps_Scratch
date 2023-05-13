#!/bin/bash
## IFS 
echo "${IFS}"
echo "${IFS@Q}" 


# numbers="1 2 3 4 5"
## the result is unquoted 
# touch ${numbers}
# rm {1..5}

## the result is quoted 
# touch "$numbers"

#
# IFS=","
# numbers=1,2,3,4,5
# touch $numbers
# rm {1..5}


