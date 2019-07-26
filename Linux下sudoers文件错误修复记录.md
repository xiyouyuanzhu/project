##  linux机器严重失误以及紧急处理

## (1).添加用户：sudo adduser yuanzhu

## (2).添加用户的sudo权限 sudo vim /etc/sudoers

## Username  ALL =(ALL:ALL) ALL  

###	由于之前设定的用户名为yuanzhu1 ,故username 设为yuanzhu1,直接保存，但是文件sudoers文件支持username+数值格式，因此出现错误，发现机器上的所有用户无法使用sudo权限，又没有设定rool用户。
###	解决方法：
###	非root模式下：

###	在真机模式下运行

###	pkexec visudo 

###	将sudoers文件中的内容进行修复即可。修改完成之后直接ctrl+o保存，直接回车，ctri+x退出

###	解决问题。

###	折腾了老大一阵子才解决问题，尤其是公司里面的机器，很是头疼，记录一下！！
