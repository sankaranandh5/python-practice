for i in range (500):
    a = i%10
    b = i%100
    b = (b-a)/10
    c = i/100
    if ((a*a*a)+(b*b*b)+(c*c*c)) == i:
        print i,'is a armstrong number'