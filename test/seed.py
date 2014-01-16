# initialize seed data for testing against the database

string_keys = [

	("test::string", "test value 1")
]

list_keys = [

	("test::list", ["test", "test", "test"])

]

dict_keys = [

	("test::dict", {"key": "value"})

]

all_keys = string_keys + list_keys + dict_keys

def seed_database(redis):

	for i in string_keys:

		redis.set(i[0], i[1])

	for i in list_keys:
			
		redis.lpush(i[0], i[1])

	for i in dict_keys:

		redis.hmset(i[0], i[1])



