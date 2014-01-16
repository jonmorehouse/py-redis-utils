import redis

remove_conn = None

def setup(**kw):

	# if no connection passed in create one!
	if not kw.get("redis_conn"):

		# initialize a connection
		redis_conn = redis.StrictRedis(host = kw.get("host"), port=int(kw.get("port")))
			
		remove_conn = True

	# a valid connection was passed in -- we want to keep alive!
	else:

		redis_conn = kw.get("redis_conn")

	# now update the kwargs
	kw["redis_conn"] = redis_conn

	return kw

def breakdown(**kw):

	# check if cleanup needed
	if remove_conn and kw.get("redis_conn"):

		# close the connection to our database
		kw.get("redis_conn").close()


