
from random import randint
from time import time


def insertionSort(li):
	for index in range(1, len(li)):

		currentVal = li[index]
		position = index

		while position > 0 and li[position-1] > currentVal:
			li[position] = li[position-1]
			position = position-1

		li[position] = currentVal



#myList = [87,33,105,31,54,391,3103,123,431,54,1,8,5]
#print("Before: ", myList)
#insertionSort(myList)
#print("After: ", myList)

bigList = []
for _ in range(0,16000):
	bigList.append(randint(0,5000))

################
################
startT = time()
print("Starting the sort!")
################
insertionSort(bigList)
################
endT = time()
################
timeElapsed = endT - startT
################
################
print("Time elapsed: ", timeElapsed)
