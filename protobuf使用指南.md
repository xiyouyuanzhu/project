###  Protobuf 入门   
###  基本流程为：  
1.编写proto文件   
2.编译编写好的proto文件，具体的：在当前目录下执行 ：protoc --python_out=./<地址>  <需要编译的proto文件>  
3.引用生成的xxxpb2.py文件。   

### 详见案例 
 syntax="proto3";  
 message SearchReaquest   
{   
  string query=1;   
  int32  page_number =2 ;    
  int32  result = 3 ; 	    
}     


**说明**     
 
1.在开头中注明syntax="proto3";意为制定消息类型。    
2.指定字段类型，stirng  ,int32  , 其中也可以为枚举或者是其他的消息类型 。    
3.分配字段编号，需要注意的是 ，每个字段都有一个唯一的编号，字段编号用于二进制格式来识别的字段，1-15 方位内的字段编号需要一个字节来编码，其中包括字段编号和字段类型 。       
16-2047范围内的字段需要两个字节。       
4.制定字段规则 ：     
 常用repeated字段，表示字段可以重复多次，也可以0次。        
5。注释规则与c/c++类似为//。    



