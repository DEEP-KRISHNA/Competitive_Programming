"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [-1]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
        # Your code goes here
        hashv = self.calculate_hash_value(string)
        self.table[hashv] = string
        # pass
        
    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        # Your code goes here
        hashv = self.calculate_hash_value(string)
        return(self.table[hashv])
        # pass

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        # Your code goes here
        return ord(string[0])*100 + ord(string[1])
        # pass

if __name__ == "__main__":
    hash_table = HashTable()
    print(hash_table.calculate_hash_value('UDACITY'))
    print(hash_table.lookup('UDACITY'))
    print(hash_table.lookup('UDACITY'))
    print(hash_table.calculate_hash_value('UDACIOUS'))
    


