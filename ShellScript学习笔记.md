## 1.linux日期

date=(date  --date="5 days ago" +%Y%m%d)

调用命令$(command)命令

 五天前的日期。

## 2.读取命令

${date}

##  3.使用命令source sh01.sh 和在bash下正常执行sh01.sh 不同：

使用source 执行的shell，则在父进程的bash内也可调用shell中的变量。

## 4.shell 脚本参数格式

例如：
sh04.sh   para1     para2   para3  para4

$0            $1          $2         $3       $4

(1)$0为脚本名称，$1  $2 $3 为脚本参数对应para1 para 2 para3  ...

(2)特殊的$# 为参数个数，例子中的$#为4个

(3)$*为参数全部，"$1$2$3$4" "para1 para2 para3  para4 "

(4)$@ 表示独立参数 "$1" "$2" "$3" "$4"     "para1" "para2" "para3" "para4"

## 5 .shell 参数偏移shift  默认偏移1个参数

例如：

sh01.sh  one two three four

shift 

$# =3

$* ="two" 'three' "four"

再次

shift 2

$# =1

$*='four'

## 6.条件判断式 

类似C 

if []  && /||  []  ; then

       语句

elif []  ; then 

   语句

else 

  语句



