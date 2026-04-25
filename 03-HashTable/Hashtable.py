class Hashtable:
    def __init__(self, size):
        self.buckets = size
        self.hashmap = [[] for i in range(self.buckets)]

    def __str__(self):
        return str(self.__dict__)
    # __str__ is special method that defines what should be displayed when you print your object
    # Here we are using __dict__ to print our objects in a dictionary manner.
    # i.e {'bucket': 16, 'hashmap': [[], [], [], [['ora', 300]], [], [['banana', 200]], [['grapes', 1000]], [], [], [], [], [], [], [], [], []]}


    def hash(self, key):
        return len(key) % self.buckets
        # the modulus funcion wraps the values so the hash is always between 0 to buckets-1.
        # The above line is just one of the many ways of hashing.

    def add(self, key, value):
        hash_value = self.hash(key)
        # The above line uses key given. it hashes the key and use the hashed value as index to insert in hashmap.
        reference = self.hashmap[hash_value]
        # The above line get holds of the bucket where you wish to add your key & value pair
        for i in range(len(reference)):
            if reference[i][0] == key:
                reference[i][1] = value
                return None
        # The above loop is to update the value if it already exists.
        # The loop just checks each element inside 'reference'. Each element is a key, value pair.
        # So it checks the first value(key), [i][0].
        reference.append([key, value])
        # The above line appends the key, value pair if it doesn't exist.
        return None

    def get(self, key):
        hash_value = self.hash(key)
        reference = self.hashmap[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                return reference[i][1]
        return -1
        # returns -1 if the key doesn't exist

    def delete(self, key):
        hash_value = self.hash(key)
        reference = self.hashmap[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                reference.pop(i)
                return None
        return None

    def contains(self, key):
        hash_value = self.hash(key)
        reference = self.hashmap[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                return True
        return False

# You are returning None for add and delete because they don't return anything and just add or delete the value.
# So you are making it clear that they are returning nothing

ht = Hashtable(16)
print(ht)
ht.add("syed", "100")
ht.add('apples', 10)
ht.add('ora', 300)
ht.add('banana', 200)
print(ht)
print(ht.get("ora"))
ht.delete("banana")
print(ht)