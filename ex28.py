import random
class animal(object):
    def __init__(self,name):
        self.name = name
        print 'calling parent constructor'
    def disease(self,hit):
        self.disease = 'rabis'
        self.hit = hit
class dog(animal):
    def __init__(self,name,breed,hit):
        super(dog,self).__init__(name)
        super(dog,self).disease(hit)
        self.breed = breed
        print 'calling child constructor'
dk = dog('cod','german',97)
print dk.name
print dk.disease
print dk.hit


