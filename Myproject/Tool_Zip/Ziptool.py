import zipfile
import os

def Zip(SrcDir,zfile):
    headpath =os.path.dirname(SrcDir)
    f=zipfile.ZipFile(zfile,'w',zipfile.ZIP_DEFLATED)
    for fileroot,filedir,filelist in os.walk(SrcDir):
        filePath = fileroot.replace(headpath,'')
        print('filepath=',filePath)
        f.write(fileroot,filePath)
        for file in filelist:
            print('{} is zip to {}'.format(file,filePath+'/'+file))
            f.write(os.path.join(fileroot,file),os.path.join(filePath,file))
def testZip():
    SrcDir = '/home/zhuzi166/workspace/project/Myproject'
    Zip(SrcDir,'ttt.zip')

path =os.path.join(os.getcwd(),os.pardir)
def Loop_File(pathfile):
    if os.path.isdir(pathfile):
        for file in os.listdir(pathfile):
            if os.path.isdir(pathfile):
                Loop_File(pathfile+'/'+file)
            else:
                print(file)
    else:
        print('{} is a file  not a dir'.format(pathfile))

def t1():
    path = os.path.join(os.getcwd(),os.pardir)
    print('path=',path)
    for file in os.listdir(path):
        print(file)

if __name__ == '__main__':
     Loop_File(path)
