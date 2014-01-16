# initialize version
__version__ = "0.0.1"
VERSION = tuple(map(int, __version__.split('.')))

from clear import clear
from dump import dump, dump_to_file
from load import load

__all__ = [
	
	clear,
	load,
	dump, 
	dump_to_file
]
