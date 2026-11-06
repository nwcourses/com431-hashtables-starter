from linkedlist import TuplesLinkedList
class HashTable:
	def __init__(self, nbuckets):
		self.nbuckets =  nbuckets
		self.buckets = [TuplesLinkedList() for i in range(nbuckets)]

	def calc_hash_code(self, key):
		hash_code = 0
		for i in range(len(key)):
			hash_code += 31**i * ord(key[i])
		return hash_code

	def get(self, key):
		bucket = self.calc_hash_code(key) % self.nbuckets
		return self.buckets[bucket].find(key)

	def put(self, key, value):
		bucket = self.calc_hash_code(key) % self.nbuckets
		self.buckets[bucket].add(key, value)


ht = HashTable(17)
ht.put("cat", "furry animal which goes meow")
ht.put("act", "to perform")
print(ht.get("cat"))
print(ht.get("act"))

ht2 = HashTable(31)
ht2.put("Q10201","Andrea")
ht2.put("Q12321","Barry")
ht2.put("Q14442","Chantal")
ht2.put("Q25343","Dexter");
ht2.put("Q34531","Erin")
ht2.put("Q09878","Fernand")
ht2.put("Q11333","Gabrielle");
ht2.put("Q22224","Humberto")
ht2.put("Q11144","Imelda")
ht2.put("Q54555","Jerry")
ht2.put("Q25856","Karen");
ht2.put("Q43334","Lorenzo");		 

print([bucket.size for bucket in ht2.buckets])
		
