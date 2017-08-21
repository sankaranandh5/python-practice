class name(object):

    def setint(self,ival):
        self.ival = ival
    def getint(self):
        return self.ival
obj = name()
obj.setint(58)
print obj.getint()