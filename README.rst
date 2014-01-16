Py-Redis-Utils
==============

Useful when a seeded redis database is needed during test-cycles

Overview
--------

-  helpers for seeding / clearing local redis databases during testing
-  Functions
-  dump\_to\_file(path, redis\_conn = None, host = "localhost", port=
   6379 ) - create a pickled dump of redis
-  load\_from\_file(path, redis\_conn = None, host = "localhost", port=
   6379 ) - load a pickled file into redis
-  clear(redis\_conn = None, host = "localhost", port= 6379 ) - clear a
   redis database
-  This is good for any testing environment and works well in a setup /
   breadkown Nose testing environment

