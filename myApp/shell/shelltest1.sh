#! /bin/bash

a=1
b=5

echo "a=$a"
echo "b=$b"

result=`expr $a + $b`
echo "a+b=$result"

c="shell script, calculating test"
echo "$c"
