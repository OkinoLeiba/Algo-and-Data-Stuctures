import typing

class DynamicArray:
    def __init__(self, values: typing.Optional[typing.List[typing.Any]] = None) -> None:
        self.value = values # if an array of values is passed with null option
        self.varray = [typing.Any] 
        self.len = len(self.varray)
        self.size = 0


    def create_array(self) -> list:
        self.varray = [typing.Any] * 10
        for i in range(10):
            self.varray[i] = i  
            self.size += 1
        return self.varray
         
    
    def resize_array(self) -> list:
        self.size += 1
        self.varray = [typing.Any] * self.size
        return self.varray
    
    def insert_front(self, value: typing.Any) -> list:
        # tarray = []
        # for i in range(len(self.varray)):
        #     tarray[i] = self.varray[i]
        tarray = self.varray.copy()
        self.resize_array()
        self.varray[0] = value
        for v in tarray:
            self.varray[tarray.index(v)+1] = v
        return self.varray
    
    def insert_back(self, value: typing.Any) -> list:
        # tarray = []
        # for i in range(len(self.varray)):
        #     tarray[i] = self.varray[i]
        tarray = self.varray.copy()
        # self.varray[0] = value
        self.resize_array()
        for k,v in enumerate(tarray):
            self.varray[k] = v
        self.varray[len(self.varray)-1] = value
        return self.varray
    
    def insert_index(self, value: typing.Any, index: int) -> list:
        for i in range(len(self.varray)):
            if i == index:
                temp = self.varray[i-1:len(self.varray)-1]
                carray = self.varray.copy()
                self.resize_array()
                self.varray[i] = value
                index += 1
                
            
                for j in range(len(temp)):
                    self.varray[j] = carray[j]
                    self.varray[index+j] = temp[j]   
            # exit()
                break

        # for k in range(len(carray)):
        #         self.varray[k] = carray[k]

        return self.varray
    

    @property
    def index_getter(self, value: typing.Optional[typing.Any]) -> int:
        property.fget(self.varray.index(value))
        return self.varray.index(value)
    
    @property
    def index_setter(self, value: typing.Optional[typing.Any], index: int) -> None:
        # property.fset(self.varray[index] = value)
        self.varray[index] = value

    @property
    def current_arrLen(self) -> int:
        return self.len

    
    def size_of_array(self) -> int:
        len(self.varray)
        count = 0
        for v in self.varray:
            count += 1
        return self.size
    
    def is_empty(self) -> bool:
        return len(self.varray) != 0
        self.size != 0
    
    def clear_array(self) -> None:
        # del self.varray
        # self.varray.clear()
        for i in range(len(self.varray)):
            self.varray.pop(0)
        if self.is_empty() == True:
            print("Array was not cleared!")
    
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
    dynamicArray.insert_front(3)
    dynamicArray.insert_back(3)
    dynamicArray.is_empty()
    dynamicArray.stringfy() 
    dynamicArray.insert_index(3, 6)
    dynamicArray.clear_array()

#  read-only of online my coursera project
#  https://hub.labs.coursera.org:443/connect/sharedjteqndmv?forceRefresh=false&path=%2Fnotebooks%2FSocialMediaDataAnalysis.ipynb&isLabVersioning=file-prep

# kaggle datasets download -d gpreda/covid19-tweets