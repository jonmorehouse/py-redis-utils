from os import environ
import nose

from bootstrap import redis_conn as redis
from bootstrap import REDIS_HOST, REDIS_PORT
from seed import all_keys
import redis_utils
from base_test import BaseTest


class TestClear(BaseTest):

  def setup(self):

    # lets make sure that we have seeded the database properly
    pass

    
  def testClear(self):

    # clear the database
    redis_utils.clear(host = REDIS_HOST, port = 6379)

    assert len(redis.keys()) == 0
    
