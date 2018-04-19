import random, time


from sort import shellSort, insertionSort

def timeSortFunction( list_size, sort_function, sort_name ):
    # Make random list:
    mylist=[]
    for i in range(list_size):
       mylist.append( random.randint(1,100) )

    # Sort it:
    t1 = time.time()
    sort_function( mylist )
    t2 = time.time()

    print( "{} took {:.4f} seconds for size {}".format( sort_name, t2-t1, list_size ) )


timeSortFunction( 100000,  shellSort, "Shell sort" )
timeSortFunction( 200000,  shellSort, "Shell sort" )
timeSortFunction( 400000,  shellSort, "Shell sort" )
timeSortFunction( 800000,  shellSort, "Shell sort" )
timeSortFunction( 1600000, shellSort, "Shell sort" )
#timeSortFunction( 100000, insertionSort, "Insertion sort" )

#  1.2053 / 0.5504  = 2.1898
#  2.8285 / 1.2053  = 2.3467
#  6.3732 / 2.8285  = 2.2532
#  14.5423 / 6.3732 = 2.2817
# -> cirka 2,2-2,3 times?

