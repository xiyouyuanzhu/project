import os
class Algorithm(object):
    def __init__(self,n1=0,n2=0):
        self.n1= n1
        self.n2=n2
    def result(self):
        pass
class AlgorithmAdd(Algorithm):
    def result(self):
        print('{}+{}={}'.format(self.n1,self.n2,self.n1+self.n2))
class AlgorithmDelete(Algorithm):
    def __init__(self):
        super(Algorithm,self).__init__()
    def result(self):
        print('{}-{}={}'.format(self.n1,self.n2,self.n1-self.n2))
class Factory:
    def __init__(self):
        pass
    def Choose(self,ens):
        if(ens=='+'):
            return AlgorithmAdd()
        elif(ens=='-'):
             return AlgorithmDelete()

if __name__ == '__main__':
    factory = Factory()
    oper=factory.Choose('+')
    oper.n1=1
    oper.n2=3
    oper.result()

