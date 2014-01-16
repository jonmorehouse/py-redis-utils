Py-Redis-Utils
==============

Useful when a seeded redis database is needed during test-cycles

Overview
--------

* helpers for seeding / clearing local redis databases during testing
* Functions
  * dump_to_file(path, redis_conn = None, host = "localhost", port= 6379 ) - create a pickled dump of redis
  * load_from_file(path, redis_conn = None, host = "localhost", port= 6379 ) - load a pickled file into redis
  * clear(redis_conn = None, host = "localhost", port= 6379 ) - clear a redis database
* This is good for any testing environment and works well in a setup / breadkown Nose testing environment


