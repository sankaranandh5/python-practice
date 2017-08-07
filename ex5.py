import random
import sys
import os
moneyinvested = input('enter the money invested:' )
interest = input('enter the rate of interest:' )

moneyinvested = float(moneyinvested)
interest = float(interest) * .01

for i in range(10):
    moneyinvested = moneyinvested+(moneyinvested*interest)

print  'investment after 10 years is %.2f' %(moneyinvested)




