import random

'''
Roll 21 6-sided dice. Store them in a zero-based array. Use them like such:
  Dice 16-21 (i.e., indices 15-20) represent the 3rd pool
  Dice 10-15 represent the 2nd pool
  Dice 4-9 represent the 1st pool
  Die 3 tells which die to use from the 3rd pool
  Die 2 tells which die to use from the 2nd pool
  Die 1 tells which die to use from the 1st pool
'''

log_level = 1

aDice = []

for ii in range(21):
	aDice.append(random.randint(1, 6))
	if(log_level >= 3):
		print("Die number {} = {}.".format(ii, aDice[ii]))

if(log_level >= 2):
	print("First three: {}, {}, {}.".format(aDice[0], aDice[1], aDice[2]))

iDie1Number = 2 + aDice[0]
iDie1Value = aDice[iDie1Number]
if(log_level >= 2):
	print("First die used = {}. Its value is {}.".format(iDie1Number, iDie1Value))

iDie2Number = 8 + aDice[1]
iDie2Value = aDice[iDie2Number]
if(log_level >= 2):
	print("Second die used = {}. Its value is {}.".format(iDie2Number, iDie2Value))

iDie3Number = 14 + aDice[2]
iDie3Value = aDice[iDie3Number]
if(log_level >= 2):
	print("Third die used = {}. Its value is {}.".format(iDie3Number, iDie3Value))

if(log_level >= 1):
	print(str(aDice[2 + aDice[0]]) + str(aDice[8 + aDice[1]]) + str(aDice[14 + aDice[2]]))
