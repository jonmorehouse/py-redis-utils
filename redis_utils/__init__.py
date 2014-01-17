# initialize version
with open("version", "r") as f:
    
    VERSION = tuple(map(int, f.read().split()))

from clear import clear
from dump import dump, dump_to_file
from load import load_from_file

__all__ = [
	
	clear,
	load_from_file,
	dump, 
	dump_to_file
]
