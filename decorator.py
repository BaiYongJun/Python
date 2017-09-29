#-*-coding:utf8-*-
def foo(f):
    def inner() :
        print '这是切面'
        return f()

    return inner()



@foo
def f():
    print '这是正事儿'