class demo(object):
    def __init__(self,ivalue):
        try:
            ivalue = int(ivalue)
        except ValueError:
            ivalue = 0

        self.ivalue = ivalue
    def increment(self):

        self.ivalue+=1
        print self.ivalue

obj = demo(45)

obj.increment()
obj.increment()
print obj.ivalue

