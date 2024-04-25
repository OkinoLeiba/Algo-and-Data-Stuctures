import typing

class DynamicArray:
    def __init__(self, values: typing.Optional[typing.List[typing.Any]] = None) -> None:
        self.value = values
        self.varray = [typing.Any] 
        self.size = 0


    def create_array(self) -> list:
        self.varray = [typing.Any] * 10
        for i in range(10):
            self.varray[i] = i  
            self.size += 1
        return self.varray
         
    
    def resize_array(self) -> list:
        self.varray = [typing.Any] * (self.size + 1)
        return self.varray
    
    def insert_front(self, value: typing.Any) -> list:
        # tarray = []
        # for i in range(len(self.varray)):
        #     tarray[i] = self.varray[i]
        tarray = self.varray.copy()
        self.resize_array
        self.varray[0] = value
        for v in tarray:
            self.varray[tarray.index(v)+1] = v
        return self.varray
    
    def insert_back(self, value: typing.Any) -> list:
        # tarray = []
        # for i in range(len(self.varray)):
        #     tarray[i] = self.varray[i]
        tarray = self.varray.copy()
        self.resize_array
        self.varray[0] = value
        for k,v in enumerate(tarray):
            self.varray[k] = v
        self.varray[-len(tarray)] = value
        return self.varray
    
    def insert_index(self, value: typing.Any, index: int) -> list:
        for i in range(len(self.varray)):
            if i == index:
                temp = self.varray[i:len(self.varray)-1]
                self.size_of_array
                self.varray[i] = value
                continue
            j = 0
            self.varray[i] = temp[j]
            j += 1
        return self.varray

    
    def size_of_array(self) -> int:
        len(self.varray)
        count = 0
        for v in self.varray:
            count += 1
        return self.size
    
    def is_empty(self) -> bool:
        len(self.varray) == 0
        return self.size <= 0
    
    def clear_array(self) -> None:
        del self.varray
        self.varray.clear()
        for v in self.varray:
            self.varray.remove(v)
    
    def stringfy(self) -> list:
        sarray = []
        for v in self.varray:
            if type(v) != str:
                sarray.append(str(v))
            else:
                sarray.append(v)
        return sarray
            

        
        

if '__main__' == __name__:
    dynamicArray = DynamicArray()
    dynamicArray.create_array()