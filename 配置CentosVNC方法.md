# 配置VNC 实录

##   1.安装GNOME Desktop
       1 列出的组列表里有GNOME Desktop。
	 yum grouplist
	 #安装之
	 yum groupinstall -y "GNOME Desktop" 
	 # 安装完成后，修改默认启动方式为图形化界面
	 systemctl set-default graphical.target  //设置成图形模式 
	 # 如果要换回来 
	 systemctl set-default multi-user.target  //设置成命令模式 
	 #然后重启系统即可
##  2.安装VNC
       1.yum install tigervnc-server -y #安装
       2.rpm -qa|grep tigervnc-server  #验证安装的准确性
##  3.复制vnc的启动操作脚本, vncserver@:1.service中的：1表示"桌面号"，启动的端口号##   就是5900+桌面号，即是5901，如果再有一个就是2啦，端口号加1就是5902，以此类推
      cp /lib/systemd/system/vncserver@.service /etc/systemd/system/vncserver@:1.service

##   4.配置 /etc/systemd/system/vncserver@:1.service
    vim /etc/systemd/system/vncserver@\:1.service
    找到其中的<USER> ，修改成自己的用户名，如果是root用户登录桌面就使用root用户，  如果使用普通用户登录桌面使用普通用户。
##   5.设置vnc密码，执行su cy，切换到刚配置文件设置的cy用户，执行（这一步是在cy用户##    下操作），输入两次密码，输入完成后会提示是否设置view-only password（“View-##     only   password”密码，只允许查看,无控制权限。）这个可设可不设：
     vncpasswd
##    6.启动服务 
      vncserver ； 
      /home/usr/.vnc 下查看端口
##    7.关闭防火墙
     //临时关闭
     systemctl stop firewalld
     //禁止开机启动
     systemctl disable firewalld
     //检查防火墙状态
     service iptables status
##   8.启动vnc 
    可以从桌面的vncview 启动.
 
		


