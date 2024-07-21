#include <stdio.h>
#include <stdlib.h>


int* quickSort(int* deck, int deckSize) {
    if (deckSize <= 1) {
        return deck;
    }

    int pivot = deck[deckSize / 2];
    int* left = (int*)malloc(sizeof(int) * deckSize);
    int* right = (int*)malloc(sizeof(int) * deckSize);

    int leftSize = 0;
    int rightSize = 0;

    for (int i = 0; i < deckSize; i++) {
        if (i == deckSize / 2) {
            continue;
        }
        if (deck[i] > pivot) {
            left[leftSize++] = deck[i];
        } else {
            right[rightSize++] = deck[i];
        }
    }

    left = quickSort(left, leftSize);
    right = quickSort(right, rightSize);

    for (int i = 0; i < leftSize; i++) {
        deck[i] = left[i];
    }

    deck[leftSize] = pivot;

    for (int i = 0; i < rightSize; i++) {
        deck[leftSize + 1 + i] = right[i];
    }

    free(left);
    free(right);

    return deck;
}


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* deckRevealedIncreasing(int* deck, int deckSize, int* returnSize) {
    deck = quickSort(deck, deckSize);

    int* returnArray = (int*)malloc(sizeof(int) * deckSize);
    int returnArraySize = 0;

    for (int i = 0; i < deckSize; i++) {
        if (i == 0) {
            returnArray[deckSize - 1] = deck[i];
            returnArraySize++;
        } else {
            int last = returnArray[returnArraySize - 1];

            for (int j = returnArraySize - 1; j > 0; j--) {
                returnArray[j] = returnArray[j - 1];
            }

            returnArray[0] = last;
            returnArray[1] = deck[i];
            returnArraySize++;
        }
    }

    return returnArray;
}

int main() {
    int deck[] = {17, 13, 11, 2, 3, 5, 7};
    int deckSize = 7;
    int returnSize = 0;

    int* returnArray = deckRevealedIncreasing(deck, deckSize, &returnSize);

    for (int i = 0; i < deckSize; i++) {
        printf("%d ", returnArray[i]);
    }

    free(returnArray);

    return 0;
}
