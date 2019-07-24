#!/bin/bash

read -p 'Input your name' name

case "$name" in 
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

