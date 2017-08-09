name = ''
for i in range(10):
    name = input(str('enter employee name:'))
    hours = int(input('how many hours he worked:'))
    print 'employee name is',name
    print 'and he worked for',hours,'hours totally'

    if (hours>40):
        ot = (hours - 40)*12
        print 'he gets an ot sal of',ot,'rupees\n'

    else:
        print 'he didnt get any extra salary'