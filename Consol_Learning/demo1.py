import argparse
import pexpect

class startAct(argparse.Action):
    print('startAct running')
    def __call__(self, parser, namespace, values, option_string=None):

        print(namespace)
        child = pexpect.spawn('/bin/bash',['-c','firefox'])
        index= child.expect([pexpect.EOF,pexpect.TIMEOUT])
        if index==0:
            print('>>>0')
        elif index==1:
            print('>>>1')
        else:
            print('else running')



''''
  # =====================================
    # Command line argument parsing methods
    # =====================================
    def parse_args(self, args=None, namespace=None):
        args, argv = self.parse_known_args(args, namespace)
        if argv:
            msg = _('unrecognized arguments: %s')
            self.error(msg % ' '.join(argv))
        return args

    def parse_known_args(self, args=None, namespace=None):
        if args is None:
            # args default to the system args
            args = _sys.argv[1:]
        else:
            # make sure that args are mutable
            args = list(args)

        # default Namespace built from parser defaults
        if namespace is None:
            namespace = Namespace()

        # add any action defaults that aren't present
        for action in self._actions:
            if action.dest is not SUPPRESS:
                if not hasattr(namespace, action.dest):
                    if action.default is not SUPPRESS:
                        setattr(namespace, action.dest, action.default)
'''
def t1():
    parse = argparse.ArgumentParser(description='Crawler tool')
    parse.add_argument('-s','--start',action='store',help='-s >>>start',required =True)
    args = parse.parse_args()
    print(args)


#https://blog.csdn.net/u013946404/article/details/78188266
class fooAction(argparse.Action):
        def __init__(self,option_strings,dest,nargs=None,help=None,**kwargs):
            super(fooAction,self).__init__(option_strings,dest,**kwargs)
        def __call__(self, parser, namespace, values, option_string=None):
            print('namespace={}\n values={}\n option_string={}'.format(namespace,values,option_string))
            setattr(namespace,self.dest,values)


def t2():
    parser=argparse.ArgumentParser(description='Mytool')
    parser.add_argument('-f','--foo',action=fooAction)
    args=parser.parse_args()
    print('args=',args)

class killAction(argparse.Action):

    # def __init__(self, option_strings, dest, nargs=None, help=None, **kwargs):
    #     super(killAction, self).__init__(option_strings, dest, **kwargs)

    def __init__(self,option_strings,dest,nargs=None ,**kwargs):
        super(killAction,self).__init__(option_strings,dest,**kwargs)
        # super(FooAction, self).__init__(option_strings, dest, **kwargs)

    #
    # def __call__(self, parser, namespace, values, option_string=None):
    #     print('values=',values)
    #     print('namespace={}\n values={}\n option_string={}'.format(namespace, values, option_string))
    #     setattr(namespace, self.dest, values)


    def __call__(self, parser, namespace, values, option_string=None):
        print('values',values)
        child=pexpect.spawn('/bin/bash',['-c',values],encoding='utf-8')
        child.expect(pexpect.EOF)
        print(child.before)

class ConnectAction(argparse.Action):

    # def __init__(self, option_strings, dest, nargs=None, help=None, **kwargs):
    #     super(killAction, self).__init__(option_strings, dest, **kwargs)

    def __init__(self,option_strings,dest,nargs=None ,**kwargs):
        super(ConnectAction,self).__init__(option_strings,dest,**kwargs)
        # super(FooAction, self).__init__(option_strings, dest, **kwargs)

    #
    # def __call__(self, parser, namespace, values, option_string=None):
    #     print('values=',values)
    #     print('namespace={}\n values={}\n option_string={}'.format(namespace, values, option_string))
    #     setattr(namespace, self.dest, values)


    def __call__(self, parser, namespace, values, option_string=None):
        child=pexpect.spawn('/bin/bash',['-c','ssh zhuzi166@127.0.0.1 '],encoding='utf-8')
        child.expect(pexpect.EOF)
        print(child.before)


def TinyTool():
    parser = argparse.ArgumentParser(description='Mytool')
    parser.add_argument('-s', '--start', action=killAction,help='-s  funcname ---->-s  firefox')
    parser.add_argument('-c', '--connect', action=ConnectAction,help='-c  funcname ---->connect the target PC',nargs='?')
    args = parser.parse_args()
    print('args=', args)

if __name__ == '__main__':
    TinyTool()