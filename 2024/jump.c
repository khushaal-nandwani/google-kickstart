#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>

bool canJump(int* nums, int numsSize) {
    int max_reach = 0;

    if (numsSize == 1) {
        return true;
    }

    for (int i = 0; i < numsSize; i++)
    {
        int reachable = i + nums[i];

        if (max_reach >= i && nums[i] < 1) {
            if (max_reach >= numsSize - 1) {
                return true;
            }
            return false;
        }

        if (reachable > max_reach) {
            max_reach = reachable;
        }
    }

    if (max_reach >= numsSize - 1) {
        return true;
    }
    else {
        return false;
    }
}

int main() {
    int nums[] = {2, 0}; // Example array, modify as needed
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    if (canJump(nums, numsSize)) {
        printf("Can jump to the end.\n");
    } else {
        printf("Cannot jump to the end.\n");
    }

    return 0;
}