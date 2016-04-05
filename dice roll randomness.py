import random
import numpy
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
from scipy import stats

n=1000

diceRoll = ('One', 'Two', 'Three', 'Four', 'Five', 'Six')

diceDiff = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine','Ten', 'Eleven', 'Twelve' )

def failrate(num, guess):
		diff=num-guess
		success.append(diff)

countdown=n

#Method 1: this code randomly provides an integer from 1 to 6, twice.
count=0
dicecount=dict()
dicecompare=dict()
diceadd=[]

while countdown>0:
	countdown=countdown-1
	num=random.randint(1,6)
	if num not in dicecount:
		dicecount[num]=0
	else:
		dicecount[num]=dicecount[num]+1

	numtest=random.randint(1,6)
	
	diceless=num+numtest
	diceadd.append(diceless)


	if diceless not in dicecompare:
		dicecompare[diceless]=0
	else:
		dicecompare[diceless]=dicecompare[diceless]+1

	count=count+1
	


#Method 2: this code random shuffles the diceRoll list, then selects 2nd element of the list as a dice throw. It then random shuffles dice again and selects element 5.
count=0
dice = [1, 2, 3, 4, 5, 6]
dice1save=[]
dice2save=[]
compares=[]
comparedict=dict()

while count<=(n-1):
	random.shuffle(dice)
	dice1=dice[1]
	dice1save.append(dice1)
	random.shuffle(dice)
	dice2=dice[4]
	dice2save.append(dice2)
	compare=dice1+dice2
	compares.append(compare)
	if compare not in comparedict:
		comparedict[compare]=0
	else:
		comparedict[compare]=comparedict[compare]+1	
		
	count=count+1

correlation=numpy.corrcoef(dice1save, dice2save)[0, 1]
stats=stats.describe(compares)
#stats2=stats.describe(diceadd)

correlation2=numpy.corrcoef(compares, diceadd)[0, 1]

print 'Number of throws: ', n
print 'Correlation coef for 2-dice roll craps, '+str(n)+' throws: ', correlation
print 'Correlation coef for craps outcomes, shuffle method, '+str(n)+' shuffles: ', correlation2
print stats
#print 'Arrays: ', dice1save, dice2save

from scipy import stats
import numpy as np


slope, intercept, r_value, p_value, std_err = stats.linregress(dice1save,dice2save)

count=0
modErrors=[]
predictions=[]
games=[]
for i in dice2save:

	prediction=(intercept+(slope*dice1save[count]))
	modError=i-prediction

	predictions.append(prediction)
	modErrors.append(modError)
	game=count+1
	games.append(game)

	
	count = count +1

#print 'Slope: ', slope, intercept, r_value, p_value, std_err


counts=dicecompare.values()
"""
plt.plot(dice1save, dice2save, 'r--')
plt.show()
"""
def movingaverage (values, window):
    weights = np.repeat(1.0, window)/window
    sma = np.convolve(values, weights, 'valid')
    return sma

yMA = np.array(movingaverage(diceadd,2))
modErrorMA=np.array(movingaverage(modErrors,1))
"""
plt.plot(games[len(games)-len(yMA):],yMA)
plt.plot(games,diceadd)
plt.title('Dice Forecast using Moving Average Estimation Tool')
plt.ylabel('Dice rolls')
plt.xlabel('Games in order of play')
plt.show()



plt.plot(games[(len(games))-len(modErrorMA):],modErrorMA)
plt.plot(games,modErrorMA)
plt.title('Dice Model Error and Moving Average Estimation or Errors - whoite noise or not?')
plt.ylabel('Dice Model Errors')
plt.xlabel('Games in order of play')
plt.show()

dice = plt.figure()
plt.plot(games,modErrors)
plt.title('Dice prediction errors')
plt.ylabel('Game errors')
plt.xlabel('Games in order of play')
plt.show()

dice = plt.figure()
plt.plot(games,predictions)
plt.title('Dice predictions')
plt.ylabel('Dice outcomes')
plt.xlabel('Games in order of play')
plt.show()
"""
y_pos = np.arange(len(diceDiff))
outcomes = counts
error = np.random.rand(len(diceDiff))

plt.barh(y_pos, outcomes, xerr=error, align='center', alpha=0.4)
plt.yticks(y_pos, diceDiff)
plt.xlabel('Outcomes')
plt.title('Are your dice fair?')

plt.show()
