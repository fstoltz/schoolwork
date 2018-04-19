
from random import randint
from time import time

def bubbleSort(lis):

	for passnum in range(len(lis) -1, 0, -1):
		for i in range(0, passnum):
			if lis[i] > lis[i+1]:
				tmp = lis[i]
				lis[i] = lis[i+1]
				lis[i+1] = tmp





#myList = [87,33,105,31,54,391,3103,123,431,54,1,8,5]
#print("Before: ", myBigList)
#bubbleSort(myBigList)
#print("\nAfter: ", myBigList)


bigList = []
for _ in range(0,2000):
	bigList.append(randint(0,5000))

################
################
startT = time()
print("Starting the sort!")
################
bubbleSort(bigList)
################
endT = time()
################
timeElapsed = endT - startT
################
################
print("Time elapsed: ", timeElapsed)