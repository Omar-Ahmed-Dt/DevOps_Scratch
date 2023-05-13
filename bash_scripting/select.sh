#!/bin/bash
#

PS3="What the department your selected? "
select dep in sales finance engineering "customer service";do
    echo "your department is $dep"
    break 
done 


