#!/bin/bash


if [ "$#" -gt "1" ];then 
	echo "Parameter setting error stop it "
	echo "All parameter is >>>>$*"
	exit 1
fi 
data=$(./sh03.sh)
echo $data
echo "fun end"
