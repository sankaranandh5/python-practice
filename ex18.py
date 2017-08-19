class integer(object):
    def setval(self,val):
        try:
            val = int(val)
        except ValueError:
            return
        self.val = val

    def getval(self):
        return self.val

    def increment(self):
        self.val+=1

i = integer()
i.setval(10)
print i.getval()
i.increment()
print i.getval()
