import bootstrap
import pickle

# [(key, ttl, key_dump)]
def load_key(key, redis):
	
	if key[1] <= 0:
		
		redis.restore(key[0], 0, key[2])

	else:

		redis.restore(key[0], key[1], key[2])

def load_from_file(path, **kw):
	
	try:

		kw = bootstrap.setup(**kw)

	except Exception as e:

		raise e

	else:

		# initialize the redis connection
		redis_conn = kw.get("redis_conn")

		# first unpickle the file into a list of objects
		dump_data = pickle.load(open(path, "rb"))	

		for key in dump_data:

			load_key(key, redis_conn)
			
		bootstrap.breakdown(**kw)




