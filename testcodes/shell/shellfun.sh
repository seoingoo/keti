#! /bin/bash

two_sum_fun()
{
    echo "first argu : $1"
    echo "second argu : $2"
    sum=`expr $1 + $2`

    return $sum
}

echo "first argu : "
read input1

echo "second argu : "
read input2

two_sum_fun $input1 $input2
result=$?

echo "sum = $result"
