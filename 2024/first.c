#include <stdio.h>
#include <stdlib.h>
#include "uthash.h"


// The structure for the hash table
typedef struct {
    int key; 
    int index;
    UT_hash_handle hh;
} hashTable;


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    hashTable *hashTable = NULL, *element, *temp;
    int *result = (int *)malloc(sizeof(int) * 2);
    *returnSize = 2;

    for (int i = 0; i < numsSize; i++) {
        int complement = target - nums[i]

        
    }

    return result;
}

// try with Input: nums = [2,7,11,15], target = 9
// Output: [0,1]

int main() {
    int nums[] = {2, 7, 11, 15};
    int numsSize = 4;
    int target = 9;
    int returnSize;
    int *result = twoSum(nums, numsSize, target, &returnSize);
    return 0;
}