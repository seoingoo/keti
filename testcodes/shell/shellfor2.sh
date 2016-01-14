#! /bin/bash

list=`ls /etc`
count=0

for file in `echo $list`
do
    echo $file
    count=`expr $count + 1`
done

echo
echo "#file : $count"
