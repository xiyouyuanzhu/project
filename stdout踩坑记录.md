#  为了能够实现log正常检出
   采用方法为： 讲输出重定向为t.log
   调用指令： sys.stdout=f
#  切结要解除引用 ，如果需要解析输出命令行内容的时候     

   out = sys.stdout
   sys.stdout=out


