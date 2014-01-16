from os import environ
from random import choice
import nose

from bootstrap import redis_conn as redis
from bootstrap import REDIS_HOST, REDIS_PORT
from seed import all_keys
import redis_utils
from base_test import BaseTest

class TestLoad(BaseTest):

	def setup(self):

		redis_utils.clear(redis_conn = redis)
	
	def testLoad(self):

		redis.set("TEST", "TEST JON")
		
		print redis.dump("TEST")

		pass

