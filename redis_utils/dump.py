import bootstrap
import pickle

def get_key(key, redis):

	value = (
		
		key, 
		redis.ttl(key),
		redis.dump(key)
	)

	return value

def dump_to_file(path, **kw):
	
	try:
		dump_data = dump(**kw)

	except Exception as e:

		raise e

	else:

		# pickle data here
		pickle.dump(dump_data, open(path, "wb"))

def dump(**kw):

	try:
		# set up the connection wit the passed parameters
		kw = bootstrap.setup(**kw)
	
	except Exception as e:

		raise e
	else:

		redis_conn = kw.get("redis_conn")	

		dump_data = []

		# now loop through each key and remove from the database
		for key in redis_conn.keys():

			dump_data.append(get_key(key, redis_conn))

		# breakdown  test environment here
		bootstrap.breakdown(**kw)

		return dump_data



