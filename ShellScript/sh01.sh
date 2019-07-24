#!/bin/bash


#pragram    计算 1+2...+100

i=0
s=0
befor_data=`date +%s`
echo "befor_data>>>>$befor_data"
while [ "$i" != "100" ]
do
   i=$((i+1))
   s=$((s+i))
done

end_data=`date +%s`
echo "end_data>>>>>$end_data"

echo "func end"




