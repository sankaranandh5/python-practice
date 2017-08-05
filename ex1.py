pi = (1,2,2,5,6,5)
print pi

pi1 = list(pi)
print pi1

pi1[2] = 6
print pi1

pi = tuple(pi1)
print pi

print len(pi),max(pi),min(pi)

pi3 = pi + tuple(pi1)
print pi3