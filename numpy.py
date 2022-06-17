added = a+b #elementwise
added_in_the_end = np.concatenate(a,b) #add at the end of the array
#if you want to add in multiple dimentions check the documentation of np.concatenate

# On the cmd

>>> np.append([1, 2, 3], [[4, 5, 6], [7, 8, 9]])
array([1, 2, 3, ..., 7, 8, 9])
