#!/usr/bin/python3
import sys

if __name__ == "__main__":
	argv = sys.argv[1:]
	num_args = len(argv)
	
	if num_args == 0:
		print("0 arguments.")
	else:
		if num_args == 1:
			print("1 argument:")
		else:
			print("{:d} arguments:".format(num_args))
		for index, argument in enumerate(argv, start=1):
			print("{:d}: {}".format(index, argument))
