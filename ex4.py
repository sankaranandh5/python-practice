po = {'dragonwarrior':'po',
      'master':'shifu',
      'gound':'tigeress',
      'flying':'crane'}
print po.get('master')

po['master']='ooguway'
print po

del po['master']
print po.get('master')
print po.get('flying')

print po.keys()
print po.values()
print len(po)

