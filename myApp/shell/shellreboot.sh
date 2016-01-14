#! /bin/bash

until [ \( $select -eq 1 \) -o \( $select -eq 2 \) ]
do
    echo
    echo "1. System Reboot Reservation."
    echo "2. Cancel the Reservation."
    echo "Select : "
    read select
done

if [ $select -eq 1 ]
then
    echo
    echo "Input the minutes : "
    read min
    echo

    sudo shutdown -r -t sec $min 'System Reboot'

    echo "System Reboot after $min seconds!"
    echo
elif [ $select -eq 2 ]
then
    echo
    
    sudo shutdown -c
    echo "Complete to cancel the reboot reservation!"
    echo
fi
