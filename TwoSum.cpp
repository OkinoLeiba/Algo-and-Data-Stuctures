using namespace std::vector;

class TwoSum{
public:
    vector<int> twoSumFunc(std::vector<int>& nums, int target) {
        int narray[2];
        
        for (int i = 0; i <= nums.size()-1; i++) {
            for(int j = i + 1; j <=  nums.size(); j++) {
                if (nums[i] + nums[j] == target && i != nums.size()-1) {
                    return {i, j};
                }
            };
        };
    return {};
    }
};


class TwoSum_Hash {
    public:
        vector<int> twoSum(std::vector<int>& nums, int target) {
        int n = nums.size();

        for (int i = 0; i <= nums.size()-1; i++) {
            int hashTable[nums[i]] = i;
        };

        struct Hash_items {
            int* key;
            char* value;
        };

    return {};
    }
};



int main() {

    TwoSum twoSum;

    twoSum.twoSumFunc([4,6,4,7], 10);

};

