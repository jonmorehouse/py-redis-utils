import bootstrap

def clear(**kw):

	try:
		# set up the connection wit the passed parameters
		kw = bootstrap.setup(**kw)
	
	except Exception as e:

		raise e
	else:

		redis_conn = kw.get("redis_conn")	

		# now loop through each key and remove from the database
		for key in redis_conn.keys():

			# delete the key
			redis_conn.delete(key)

		# now lets breakdown this function
		bootstrap.breakdown(**kw)

