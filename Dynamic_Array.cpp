template <typename T>
class DynamicArray{
    // initialize values and objects
    private:
        T* pointer_to_arr;
        const int size = 0;
        int capacity = 0;


    // initialize & size array and insert values
    public:
        int create_array(T arr[], int s) {
            pointer_to_arr = new int[s];
            size = s;
            
            for (int i = 0; i < size; i++) {
                pointer_to_arr[i] = arr[i];
                
            }
        }
    
    public: 
        int size_of_array() { return size;}

    public:
        bool isEmpty() {return size_of_array() == 0;}

    public:
        void capacity_of_array(int cap = size) {
            if(cap < 0) {throw new std::invalid_argument("Illegal Capacity" + cap)};
            capacity = cap;
        }

    public: 
        add_element_array(& pointer_to_arr, int value) {
            pointer_to_arr = new T[size+1];
            std::copy(pointer_to_arr.begin(), pointer_to_arr.end, pointer_to_arr);
            pointer_to_arr[size+1] = value;
            pointer_to_arr[pointer_to_arr.back()] = value;
        }
    
};


int main() {
    

    int the_arr[] = {1,2,3,4,5};

    int capacity = sizeof(the_arr)/sizeof(int);

    // DynamicArray<int> dynamicArray = DynamicArray<int>();

    DynamicArray<int> dynamicArray;

    dynamicArray.capacity_of_array();
   
};