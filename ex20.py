class dog(object):
   def __init__(self,name,height,weight):
       self.name = name
       self.height = height
       self.weight = weight
   def run(self):
       print '%s the dog runs'%(self.name)
   def eat(self,food):
       print '%s eats %s'%(self.name,food)
   def bark(self):
       print '%s the dog barks'%(self.name)

scott = dog('scott',55,56)
scott.run()
scott.eat('dog food')
