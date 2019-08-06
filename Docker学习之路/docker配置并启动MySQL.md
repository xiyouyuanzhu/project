##  记录docker 下配置并启动mysql   
##  复习 docker 介绍以及与VM对比
    docker为轻量化容器，其中存放了程序以及其依赖环境，包括程序运行的库以及其配置文件，每一个docker之间都是独立存在互不影响，公用一个OS。
    VM 为虚拟化环境，其中存放了所有程序以及其所依赖的库二进制文件，还有相应的OS。
    相比较于VM ，docker 不需要完整的OS环境和各种软件所需的依赖环境


## 言归正传：
   使用到的docker命令：

docker images   显示本地有的镜像

docker pull +镜像名称   从docker hub上面拉取镜像

docker run 
   --name  定义容器的名称

   -d  让docker容器在后台运行到

   -a 查看已经创建的容器

   -s  查看启动的容器

docker start docker_name   启动名称为docker_name的容器

docker stop docker_name   关闭名称为docker_name的容器

docker rm docker_name     删除名称为docker_name的容器

docker rmi docker_name   删除名称为docker_name的镜像

docker rename old_name new_name 给容器重命名

操作：

[root@localhost ~]# docker pull mysql   拉取镜像

[root@localhost ~]# docker images|grep mysql   查看镜像

[root@localhost ~]# docker ps -s      查看正在运行的容器
[root@localhost ~]# docker exec -it dc1c39266b16 bash
