#  调用paramiko 实现SSH连接本机时，为了实现免密登录，可以通过配置ssh 公钥以及/etc/sshd_config 配置文件  
#  实现免密登录。     
  
   
##  具体的 ：      
##  1.  ssh-keygen 建立ssh 公钥私钥       
      在/home/usr/.ssh 文件内含有 id_rsa（私钥） id_rsa.pub （公钥）      
##  2. 配置/etc/ssh/sshd_config文件   
     1.PubkeyAuthentication yes  #是否使用公钥验证   
     2,AuthorizedKeysFile      .ssh/authorized_keys  #公钥的保存位置，     
        .ssh/authorized_keys 内存放着公钥（id_rsa.pub）   
     3.PasswordAuthentication no  #禁止使用密码验证登录  
     4.RSAAuthentication yes #开启RSA验证 ，若配置文件内没有该选项 ，则手动输入配置即可  
##  3.添加authorized_keys  
    将id_rsa.pub 内容追加到 /home/usr/.ssh/authorized_keys 文件内,     
    若文件没有则新建文件直接将id_rsa.pub内容复制到authorized_keys即可
     
 ××【代码传送门】（https://github.com/xiyouyuanzhu/project/blob/master/Myproject/Auto_SSH/auto_ssh.py）××
