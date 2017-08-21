class test(object):
    var = 20

    def printing(self):
        print 'this function prints'
        print self
demo = test()
print demo.var
print test.var

demo.printing()
print demo
