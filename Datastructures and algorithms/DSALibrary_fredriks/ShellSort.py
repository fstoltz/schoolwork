from random import randint
from time import time


def shellSort(array):

	gap = len(array) // 2

	#	loop over the gaps
	while gap > 0:
		#	do the insertion sort
		for i in range(gap, len(array)):
			val = array[i]
			j = i

			while j >= gap and array[j-gap] > val:
				array[j] = array[j-gap]
				j -= gap

			array[j] = val

		gap //= 2 #	ny gap




bigList = []
for _ in range(0,2000):
	bigList.append(randint(0,5000))

################
################
startT = time()
print("\nDone filling the array!\n\tStarting the sort!")
################
shellSort(bigList)
################
endT = time()
################
timeElapsed = endT - startT
################
################
print("Time elapsed: ", timeElapsed)

#print(bigList)
