#!/bin/bash


if [ "$#" -gt "1" ];then 
	echo "Parameter setting error stop it "
	echo "All parameter is >>>>$*"
	exit 1
fi 


case "$1" in 
	"yuanzhu")
	echo "Your name is yuanzhu"
	;;
	"yuanmeng")
	echo "your name is yuanmeng"
	;;
        *)
	echo "I  dont kone who are you"
esac
echo "Func end"

