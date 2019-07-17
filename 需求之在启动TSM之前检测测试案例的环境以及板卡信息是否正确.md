#  新需求要求在启动测试站主控TSM（Test station master，TSM）之前需要对测试案例进行检测 ，这是北京分部的需求 ，他们也提前编写好了借口.sh 我们只需要正常运行，拿到返回值进行处理即可。 由于公司内网， 我大致记录一下实现以及分析过程。
#   需要执行以下几步（需进行人机交互，使用脚本来模拟人为输入指令）
    1.执行  source   env.sh  ##env.sh 含有环境变量信息     
    2.执行 run.sh  #  脚本内部含有检测函数

#    分析需求以及实现方法
##   由于是模拟人机交互 ，我首先想到的是通过os.Popen(cmd) 
     1.需要注意的是 ，第一 ，执行指令 source  env.sh 与run.sh  是分开进行的 ，然而第一条指令为添加环境变量 ，不可以同步执行的。
     2.也想到，可以通过&&同时执行两条指令 ，先配置环境变量再执行run.sh ，此方法理论上可行，但是实现有难度 为何：
     （1）查阅资料说，source指令 需要使用/bin/bash执行的，但是 Popen默认使用/bin/sh
      （2）指令繁琐 ，而且不可制定是bash 还是sh
     3.想到使用subprocess.Popen()指令 ，可以实现制定/bin/bash执行指令 ，但是没办法进行追加执行两条指令 ，故寻找其他方法实现。
##   想到同时执行两条指令，而且得读取内容 ，加之之前有学过pexpect模块人机交互，故借助项目来练手。
    1.本想着使用pexpect.spawn()直接执行指令呢 ，但是必须制定/bin/bash 
    2. 经过实际验证 ，可以这样进行指定命令行：
    **        chiild =pexpect.spawn('/bin/bash',['-c','source /etc/profile &&ls -l '] ,logfile=f,encoding='utf-8')**
    3.由于是外网环境下 ，仅仅拿来实验，验证通过有效，在内网已经按照该方法实现了自动化运行脚本 ，通过正则表达式匹配拿到返回值，实测有效。


###    (测试案例传送门)[https://github.com/xiyouyuanzhu/project/blob/master/Myproject/IsAbleStartTestJob/Isable.py]




