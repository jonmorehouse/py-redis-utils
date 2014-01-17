import os
directory = os.path.dirname(os.path.realpath(__file__))

with open("%s/version" % directory, "r") as f:
    
    VERSION = f.read()

from clear import clear
from dump import dump, dump_to_file
from load import load_from_file

__all__ = [
	
	clear,
	load_from_file,
	dump, 
	dump_to_file
]
