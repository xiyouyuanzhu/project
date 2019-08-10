#!/bin/bash
echo $(source /home/zhuzi166/workspace/project/RunnigShellAndRetrun/env.sh)
tname=$name

rnum=10
funcreturn()
{
  #echo "func running"
  #rnum=10
  return $rnum ;
}
funcreturn
