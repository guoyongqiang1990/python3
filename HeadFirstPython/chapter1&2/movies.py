movies = [
	"The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
	     ["Graham Chapman",
	        ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

if __name__=="__main__":
	for each_item in movies:
		if isinstance(each_item,list):
			for each_member in each_item:
				if isinstance(each_member,list):
					for each_actor in each_member:
						print(each_actor)
				else:
					print(each_member)
		else:
			print (each_item)