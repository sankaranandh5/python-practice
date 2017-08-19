class person(object):
    def __init__(self,name):
        self.name = name

    def revealname(self):
        print 'my name is %s'%(self.name)

class superhero(person):
    def __init__(self,name,superheroname):
        self.superheroname = superheroname
        super(superhero,self).__init__(name)

    def revealidentity(self):
        super(superhero,self).revealname()
        print '...and i am %s'%(self.superheroname)

wade = superhero('wade wilson','deadpool')
wade.revealidentity()