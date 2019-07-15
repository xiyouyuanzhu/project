#   公司服务器有多台终端，由于前天配置免密登录SSH , 今天由于TSM服务器重启，其余几台终端无法SSH连接主机
#   重置/etc/ssh/sshd_config 文件后恢复正常登录 。



#   为了实现“免密” 本次启用秘钥来登录服务器，通过调用本机的秘钥 id_rsa来连接。

#   具体流程如下：
    1.ssh-keygen  添加ssh秘钥
    2.配置/etc/ssh/sshd_config文件
       （1）：RSAAuthentication yes  #启动RSA验证
       （2）：PubkeyAuthentication yes #启动公钥，其实这项可以使本机连接本机免秘钥，前提是要按照文章《配置ssh免密登录.md》来配置
       （3）:PasswordAuthentication yes #该项要求允许密码输入

    具体paramiko 使用密钥SSH链接 代码实现见
    (案例传送门)[https://github.com/xiyouyuanzhu/project/blob/master/Myproject/Auto_SSH/SSHKeyConnect.py]
#   补充一些常用的SSH命令，包括查看运行状态 ，重启，开机启动等。
    1.  查看运行状态：systemctl status sshd.service

    2.  启动服务：systemctl start sshd.service

    3.  重启服务：systemctl restart sshd.service

    4.  开机自启：systemctl enable sshd.service