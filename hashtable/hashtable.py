class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
      


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=0):
        self.capacity =capacity
        self.size = 0
        self.storage =[None]*self.capacity
        # Your code here


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.size/self.capacity
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash =5381
        for element in key:
            hash = (( hash << 5) + hash) + ord(element)
        return hash & 0xFFFFFFFF
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity*2)
        self.size+=1
        data = HashTableEntry(key, value)
        index = self.hash_index(key)
        # go to the index of hashtable 
        location = self.storage[index]
        # check if location is empty
        if location is None:
            # then, put item there
            self.storage[index] = data
            # self.storage.insert(key, value);
        # otherwise
        else:
            if location.key == key:
                self.storage[index] = data
                return
            else:
                previous=location
                while location is not None:
                     previous = location
                     location = location.next
                previous.next = data
                
        # Your code here


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # decrement the size
        self.size -= 1
        # find the index
        index = self.hash_index(key)
        # go to location
        location = self.storage[index]
        if location is None:
            return None
        else:
            if location.next is None:
                if location.key == key:
                    location = None
                else:
                    previous=location
                    while location is not None:
                        previous = location   
                        location = location.next
                        if(location.key == key):
                            previous.next = location.next
                            location.next=None
                            break
                return None
        
       



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # find the index of key
        index = self.hash_index(key)
        # find the location 
        location = self.storage[index]
         # check if it is empty
        if location is None:
            # return None 
            return None
        else:
            # check if location is the searched item
            if location.key == key:
                return location.value
            else:
                # iterate through the linked list 
                while location is not None:
                    if location.key == key:
                        return location.value
                        break
                    # previous = location
                    location = location.next
                    
                    
                return None
                    
         
        # Your code here


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # doubled = [None] * len(self.storage) * 2
        self.capacity = new_capacity
        copy=self.storage
        self.storage = [None] * self.capacity
        for i in range(0, len(copy)):
            if (copy[i] is not None):
                while (copy[i]) is not None:
                    self.put(copy[i].key,copy[i].value)
                    copy[i] = copy[i].next
                    



        
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
