import os
from os import environ
from random import choice
import nose
import pickle

from bootstrap import redis_conn as redis
from bootstrap import REDIS_HOST, REDIS_PORT
from seed import all_keys, seed_database
import redis_utils
from base_test import BaseTest

class TestLoad(BaseTest):

	path = "temp_dump.p"

	def setup(self):
	
		seed_database(redis)
		redis_utils.dump_to_file(self.path, redis_conn = redis)
		redis_utils.clear(redis_conn = redis)

	def teardown(self):

		os.remove(self.path)
	
	def testLoad(self):
		
		# we now have an empty database!
		# now load the path file
		redis_utils.load_from_file(self.path, redis_conn = redis)
	
		# now lets verify the keys are as they should be
		assert len(redis.keys()) == len(all_keys)

		# now lets assert that the keys are as they should be
		dump_data = pickle.load(open(self.path, "rb"))

		for key in dump_data:

			assert redis.dump(key[0]) == key[2]

