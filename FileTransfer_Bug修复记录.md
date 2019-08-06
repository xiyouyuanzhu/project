##  记录FileTransfer  Bug 修复过程


## 技巧1：
  递归查找文件中含有‘Encode’的代码行：
  grep -rn 'Encode'    该命令行可以递归去检索文件中的所有py文件，打印出含有该命令行的文件以及其行号。


##  技巧2
  STP （Start Test Plan）模块，锁死问题 ，没有突破口，故查看进程树的方式，记录其进程关系，进一步排查问题所在

## 技巧4 
 最简单高效的方法莫过于通过打印log ，我们通过:
 import sys
 f=open('FTC.log','w+')
 sys.stdout=f
 指定输出为log文本FTC.log  ，这样子通过print(‘’)信息则可定位问题所在。

