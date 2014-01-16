Py-Redis-Utils
==============

Useful when a seeded redis database is needed during test-cycles

Overview
--------

* helpers for seeding / clearing local redis databases during testing
* Functions
  * dump - create a pickled dump of redis
  * load - load a pickled file into redis
  * clear - clear a redis database
  * reset - clear + seed
* This is good for any testing environment and works well in a setup / breadkown Nose testing environment
* cli -- to load / dump data from command line  



