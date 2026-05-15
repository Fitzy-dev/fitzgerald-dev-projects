# Jordan Fitzgerald
# 5/14/2026
# Hash Table Implementation


class HashTable():# Hash table class using separate chaining for collision resolution
    def __init__(self):# Initialize the hash table with an empty collection
        self.collection = {}

    def hash(self, key):# Simple hash function that sums the ASCII values of the characters in the key
        hash_value = 0

        for char in key:
            hash_value += ord(char)
        
        return hash_value
    
    def add(self, key, value):# Add a key-value pair to the hash table
        hashed_key = self.hash(key)

        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}
        
        self.collection[hashed_key][key] = value
    
    def remove(self, key):# Remove a key-value pair from the hash table
        hashed_key = self.hash(key)

        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                del self.collection[hashed_key][key]
    
    def lookup(self, key):# Look up the value associated with a key in the hash table
        hashed_key = self.hash(key)

        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                return self.collection[hashed_key][key]
        
        return None

def main(): # Test the HashTable class
    my_table = HashTable()
    my_table.add("name", "Alice")
    my_table.add("age", 30)
    print(my_table.lookup("name"))
    print(my_table.lookup("age"))
    my_table.remove("name")
    print(my_table.lookup("name"))
