def chname():
     name = 'barley'
     return name


name = 'barney'

print chname(),name

name = chname()

print name


def sum(num1,num2):
    add = num1+num2
    return add
addi = sum(5,6)
print addi

def chdname(name):
    name = 'joey'
    return name

newname = chdname('chandler')
print newname