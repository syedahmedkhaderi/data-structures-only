def hash_me(value):
    sum_of_letters = 0
    for i in value:
        sum_of_letters += ord(i)
    # ord functions gets the unicode value of the letter
    return sum_of_letters % 10

class Hashtable:
    def __init__(self):
        self.bucket = [[] for i in range(0,10)]

    def add(self, value):
        index = hash_me(value)
        self.bucket[index].append(value)
        print(self.bucket)

    def find(self, value):
        index = hash_me(value)
        bucket_list = self.bucket[index]
        if not bucket_list:
            print("Value not found")
            return
        for item in bucket_list:
            if item == value:
                print(f"Found at position {index} : {value} in Hashtable")
                return
        print("Value not found")


ht = Hashtable()
hash_me("Saara")
print(ht.bucket)
ht.add("Saara")
ht.add("syed")
ht.find("Saara")
ht.add('mia')
# ht.delete("syed")
