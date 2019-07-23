
##  1.环境变量记录：

要让父进程的变量能在子进程中继续使用，执行export 变量名称

## 2.shell 变量键盘读取，使用read 

例如，read-p （'提示内容' ）-t (时间)  atest  

           >>>>>>>>hello world 

          echo $atest

         >>>>>>>>>hello world

## 3.declare 声明变量类型

 declare  -i /-x/-a/-r  

i 为int 

x   与export 一样将其后边的参数设为环境变量

a  将变量设定为数组array 

r  设定为只读模式

-x实例：特殊的，declare -x PATH =$PATH:/地址/

补充：读取数组中的操作：

var[1]='hello'

var[2]='word'

读取操作：echo ${var[1]}

## 4.alias  lm ='ls -l | more'

设定独特命令行。

unalias lm  解除

例如alias h='history'

bash >>>> h 

## 5.数据重定向 

输出重定向

> 替换

>> 追加

输入重定向

<

<<

输入 0  ，输出1，错误2

## 6.一行执行多行命令

；，&&，||

符号解析：

；符号为前一条命令执行完成后直接执行下一条命令，不判定执行是否成功

&& 表示只有前一条指令执行完毕后才执行下一条命令

||表示当前一条命令执行正确则下一条命令不执行， 当前一条命令执行错误，则执行下一条命令。

案例：

判断文件是否存在，存在返回exist 不存在 None

ls /temp/tdir  && echo "exist" || echo "None"




