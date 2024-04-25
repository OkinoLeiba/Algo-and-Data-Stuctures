/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */


var twoSum = function(nums, target) {
    for (var i = 0; i <= nums.length-1; i++) {
        for (var j = i + 1; j <= nums.length; j++) {
            if (nums[i]+nums[j] == target) {
                return [i, j];
            }
        }
    }
}


function twoSum_Hash(nums, target) {
    var hashTable = new Object;
    for (var i = 0; i <= nums.length-1; i++) {
        hashTable[i] = nums[i];
    }
}


twoSum([[2,7,11,15]], 9);

twoSum_Hash([[3,2,4]], 5);



