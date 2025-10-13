# First we define a Trie_node class containing 26 children each initialized to None,
# and an end_of_word flag to determine whether it marks the end of a word or not
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

#We define a private helper function to calculate the numerical index of each character in the range of 0-25
    def _char_index(self, char):
        if char.isupper():
            return ord(char) - ord('A') # if char = D, D = 68, then 68 - 65 = 3. This gives index between 26
        else:
            return ord(char) - ord('a') 
        # if the char is lowercase then it gives index between 97-122 then subtract 'a' which is 97
        # to keep the value between 0-26. ex: char = 'd' = 100 --> 100 - 97 = 3.
    

#insert function:
#We will create a pointer which will start at the root node. Then for every character in the word to be inserted,
#We will check if the character already exists in the trie by matching it with the pointer's children.
#If it does, we will simply update the pointer to that child of the current node and repeat the process for the next character of the word
#Otherwise, we will initialize a new node at the index of the character that is to be inserted, which was equal to None until now,
#And then we will update the pointer to point to this newly created node and repeat the process for the next character
#Once we reach the end of the word, we will set the is_end_of_word to True for the node containing the last character.
#The entire process will take O(m) time where m is the length of the string
    def insert(self, string):
        pointer = self.root
        
        for char in string:
            index = self._char_index(char)
            if not pointer.children[index]:
                pointer.children[index] = TrieNode()
            pointer = pointer.children[index]
        pointer.is_end_of_word = True
        return

# Search method:
# Only this time, instead of creating a new TrieNode when we don't find a character in the Trie,
# we will simply return False
# And if after the loop terminates and is_end_of_word equals True and the node isn't equal to None,
# it means we have found the word
    def search(self, string):
        pointer = self.root
        for char in string:
            index = self._char_index(char)
            if not pointer.children[index]:
                return False
            pointer = pointer.children[index]
        return pointer and pointer.is_end_of_word

my_trie = Trie()
my_trie.insert('Data')
my_trie.insert("Structures")
my_trie.insert("and")
my_trie.insert("Algorithms")
print(my_trie.search("and"))
#True
print(my_trie.search("Data"))
#True
print(my_trie.search("woohoo"))
#False
print(my_trie.search("STructures"))
#True
# Both upper and lower case is converted to a value between 0-26.


# Maybe in Future when i study this further, ill add print and other methods.
# But for now this is as far as my research goes