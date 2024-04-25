import java.util.HashMap;
import java.util.Map;
 
class TwoSum {
    public int[] twoSumJava(int[] nums, int target) {
        Map<Integer, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (hashMap.containsKey(target - nums[i])) {
                return new int[] {hashMap.get(target - nums[i]), i};
            }
            hashMap.put(nums[i], i);
        }
        return new int[] {};
    }
}


twoSum = new TwoSum;
twoSum.twoSumJava([2,7,8,9], 9);