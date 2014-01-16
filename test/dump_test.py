import os
from os import environ
import nose
import pickle

# import project dependencies
from bootstrap import redis_conn as redis
from bootstrap import REDIS_HOST, REDIS_PORT
from seed import * 
import redis_utils
from base_test import BaseTest

class TestDump(BaseTest):

	def setup(self):

		seed_database(redis)

	@staticmethod
	def checkDumpData(dump):

		assert len(dump) == len(redis.keys())

		for key, dump_key in zip(redis.keys(), dump):
			
			assert key == dump_key[0]
			assert redis.ttl(key) == dump_key[1]
			assert redis.dump(key) == dump_key[2]
	
	def testDump(self):

		dump = redis_utils.dump(redis_conn = redis)

		# make sure all of our keys check out 
		TestDump.checkDumpData(dump)


	def testDumpToFile(self):
			
		path = "pickled_dump.p"

		redis_utils.dump_to_file(path = path, redis_conn = redis)
		
		# now lets unpickle the data and ensure it's integrity
		dump_data = pickle.load(open(path, "rb"))

		# check and verify the dump data was properly pickled 
		TestDump.checkDumpData(dump_data)

		# now lets clean up after ourselves here ... 
		os.remove(path)

