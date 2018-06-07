#!/usr/bin/python

from os import listdir, chmod
from stat import *
from sys import argv

def main():
	if len(argv) < 2:
		print(argv[0] + " FILE PERMISSIONS...")
		return 0
	
	file = open(argv[1], 'w')
	file.write("#!/bin/bash")
        file.close()

	chmod(argv[1], S_IEXEC | S_IXOTH | S_IXGRP | S_IREAD | S_IWRITE) 


if __name__ == "__main__":
	main()

