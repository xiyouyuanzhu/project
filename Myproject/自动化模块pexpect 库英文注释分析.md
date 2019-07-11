###   pexpect库广泛用于人机交互 ，一下内容分析下库中常用的一些函数
   
##    1.def expect    
##    (self, pattern, timeout=-1, searchwindowsize=-1, async_=False, **kw):   
      通过输入参数进行搜寻  
      
      expect 通过指定匹配模式来阻塞知道匹配到bash命令执行结果。  
      具体的pattern可以为字符串，可以是正则表达式 ，特殊的patter 可以是列表 ，因此可以   
      根据list 中的不同匹配项来请求不同的任务 。  
      特别的，pexpect.EOF(执行完毕)  非常有用，可以检测到指令是否执行完毕 。  
      例如：  
      **  TIPS   **  
      1.def test:  
      2.      child = pexpect.spawn('{}\n'.format('pip3 install pinda'))  
      3.      i = child.expect(['.*\$',pexpect.EOF,pexpect.TIMEOUT],timeout=-1)  
      4.      if i==0:  
      5.          print('run successful')  
      6.          print(child.before.decode('utf-8'))  
      7.      elif i==2:  
      8.          print('time out')  
      9.          print(child.before.decode('utf-8'))  
      10.      elif i==1:  
      11.          print('run  finish')  
      12.          print(child.before.decode('utf-8'))  
      
      其中befor和after 与expect相对应，以以上例子为例 ，判定patter ==1 即执行完毕，print(childe.before.decode('utf-8'))
      打印匹配到EOF（程序执行结束指令）之前的输出。 
      
      timout 设定为-1表示不设定超时参数。
  ####  切记 EOF指令下不可after ,因为执行结束后的语句 ， 平常情况下 打印输出，before即可,即匹配
  ####  上一条sendline(cmd)指令的结果

/**

        This seeks through the stream until a pattern is matched. The
        pattern is overloaded and may take several types. The pattern can be a
        StringType, EOF, a compiled re, or a list of any of those types.
        Strings will be compiled to re types. This returns the index into the
        pattern list. If the pattern was not a list this returns index 0 on a
        successful match. This may raise exceptions for EOF or TIMEOUT. To
        avoid the EOF or TIMEOUT exceptions add EOF or TIMEOUT to the pattern
        list. That will cause expect to match an EOF or TIMEOUT condition
        instead of raising an exception.

        If you pass a list of patterns and more than one matches, the first
        match in the stream is chosen. If more than one pattern matches at that
        point, the leftmost in the pattern list is chosen. For example::

            # the input is 'foobar'
            index = p.expect(['bar', 'foo', 'foobar'])
            # returns 1('foo') even though 'foobar' is a "better" match

        Please note, however, that buffering can affect this behavior, since
        input arrives in unpredictable chunks. For example::

            # the input is 'foobar'
            index = p.expect(['foobar', 'foo'])
            # returns 0('foobar') if all input is available at once,
            # but returns 1('foo') if parts of the final 'bar' arrive late

        When a match is found for the given pattern, the class instance
        attribute *match* becomes an re.MatchObject result.  Should an EOF
        or TIMEOUT pattern match, then the match attribute will be an instance
        of that exception class.  The pairing before and after class
        instance attributes are views of the data preceding and following
        the matching pattern.  On general exception, class attribute
        *before* is all data received up to the exception, while *match* and
        *after* attributes are value None.

        When the keyword argument timeout is -1 (default), then TIMEOUT will
        raise after the default value specified by the class timeout
        attribute. When None, TIMEOUT will not be raised and may block
        indefinitely until match.

        When the keyword argument searchwindowsize is -1 (default), then the
        value specified by the class maxread attribute is used.

        A list entry may be EOF or TIMEOUT instead of a string. This will
        catch these exceptions and return the index of the list entry instead
        of raising the exception. The attribute 'after' will be set to the
        exception type. The attribute 'match' will be None. This allows you to
        write code like this::

                index = p.expect(['good', 'bad', pexpect.EOF, pexpect.TIMEOUT])
                if index == 0:
                    do_something()
                elif index == 1:
                    do_something_else()
                elif index == 2:
                    do_some_other_thing()
                elif index == 3:
                    do_something_completely_different()

        instead of code like this::

                try:
                    index = p.expect(['good', 'bad'])
                    if index == 0:
                        do_something()
                    elif index == 1:
                        do_something_else()
                except EOF:
                    do_some_other_thing()
                except TIMEOUT:
                    do_something_completely_different()

        These two forms are equivalent. It all depends on what you want. You
        can also just expect the EOF if you are waiting for all output of a
        child to finish. For example::

                p = pexpect.spawn('/bin/ls')
                p.expect(pexpect.EOF)
                print p.before

        If you are trying to optimize for speed then see expect_list().

        On Python 3.4, or Python 3.3 with asyncio installed, passing
        ``async_=True``  will make this return an :mod:`asyncio` coroutine,
        which you can yield from to get the same result that this method would
        normally give directly. So, inside a coroutine, you can replace this code::

            index = p.expect(patterns)

        With this non-blocking form::

            index = yield from p.expect(patterns, async_=True)



/

***  ***