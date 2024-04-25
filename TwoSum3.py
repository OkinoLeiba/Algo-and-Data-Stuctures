import typing

class TwoSum(object):
    def twoSum(self, nums: typing.List = [], target: int = None) -> list:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if nums[i] + nums[i+1] == target and nums[i+1] != len(nums)-1:
               return [i, i+1]
            

class TwoSum_Hash(object):
    def __init__(self, key: typing.Hashable, value: int, capacity: int) -> None:
        # create or initialize node for hash table
        self.key = key
        self.linear_key = value ^ 2 % 5
        self.value = value
        self.node = None

        # create or initialize hash table
        self.capacity = capacity
        self.size = 0
        self.factor = 0.75
        self.hTable = [None] * capacity


    def _hash(self, key: typing.Any) -> any:
        return hash(key) % self.capacity
    

    
    def twoSum_hash(self, nums: typing.List[int], target: int) -> list:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hast_table0 = [[]]
        for k in range(len(nums)):
            hash_table0 = {}

    def create_hashTable(self, value: int) -> dict:
        hash_table = {hash(value), value}
        return hash_table
    
    def create_hashTable_objects(self, key: int, value: int) -> dict:
        hash_table = {key, value}
        pass
        

if '__main__' == __name__:
    twoSum_Hash = TwoSum_Hash(3, 3, 10)
    twoSum_Hash._hash(3)

