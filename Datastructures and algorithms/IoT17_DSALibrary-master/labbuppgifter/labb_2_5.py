import random, time


from sort import bubbleSort, insertionSort

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


timeSortFunction( 1000, bubbleSort, "Bubble sort" )
timeSortFunction( 2000, bubbleSort, "Bubble sort" )
timeSortFunction( 4000, bubbleSort, "Bubble sort" )
timeSortFunction( 8000, bubbleSort, "Bubble sort" )
timeSortFunction( 1000, insertionSort, "Insertion sort" )
timeSortFunction( 2000, insertionSort, "Insertion sort" )
timeSortFunction( 4000, insertionSort, "Insertion sort" )
timeSortFunction( 8000, insertionSort, "Insertion sort" )

