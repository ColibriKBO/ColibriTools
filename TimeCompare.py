"""
Filename:  TimeCompare
Author(s): Peter Quigley
Contact:   pquigle@uwo.ca
Updated:   2022-09-23

Used to measure the difference in timing between several functions
"""

from time import time


##############################
## Timing Single Functions
##############################

def singleFxn(fxn, *args):
	"""
	A function to measure how long it takes to execute a specific function

		Parameters:
			fxn (func): The function to be tested
			*args (any): The arguments to be used in the test

		Returns:
			dt (float): Amount of time it took to run the function
				    with the given parameters
	"""

	t = time()
	fxn(*args)
	dt = time() - t

	print("Time to run function: {}".format(dt))
	return dt


##############################
## Time Compare Functions
##############################

def twoFxn(fxn1, fxn2, *args):
	"""
        A function to compare the execution time of two functions using the same parameters

                Parameters:
                        fxn1 (func): The first function to be tested
                        fxn2 (func): The second function to be tested
                        *args (any): The arguments to be used in the test

                Returns:
			t1 (float): Amount of time it took to execute fxn1 with the given
				    parameters
			t2 (float): Amount of time it took to execute fxn2 with the given
				    parameters
			dt (float): The difference in execution time between fxn1 and fxn2
        """

	## Timing the first function

	t = time()
	fxn1(*args)
	t1 = time() - t

	## Timing the second function

	t = time()
	fxn2(*args)
	t2 = time() - t


	print("Time to run the first function: {}".format(t1))
	print("Time to run the second function: {}".format(t2))
	print("Difference in execution time:    {}".format(t2-t1))
	return t1, t2, t2-t1
