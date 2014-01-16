from os import environ
import nose

from bootstrap import redis_conn as redis
from bootstrap import REDIS_HOST, REDIS_PORT
from seed import all_keys
import redis_utils

class BaseTest(object):

	def testBadConnection(self):

		try:
			redis_utils.clear(host = "NO HOST", port = 6379)
	
		except Exception as e:

			assert True

		else:
			assert False
				

	def testPassedConnection(self):

		pass	


	def testConnectionCleanedUp(self):


		pass

