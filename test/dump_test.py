from os import environ
import nose
#import itertools

# import project dependencies
from bootstrap import redis_conn as redis
from bootstrap import REDIS_HOST, REDIS_PORT
from seed import * 
import redis_utils
from base_test import BaseTest

class TestDump(BaseTest):

	def setup(self):

		seed_database(redis)
	
	def testDump(self):

		dump = redis_utils.dump(redis_conn = redis)

		assert len(dump) == len(redis.keys())

		for key, dump_key in zip(redis.keys(), dump):
			
			assert key == dump_key[0]
			assert redis.ttl(key) == dump_key[1]
			assert redis.dump(key) == dump_key[2]

	def testDumpToFile(self):
			
		path = ".pickled_dump"

		redis_utils.dump_to_file(path = path, redis_conn = redis)


