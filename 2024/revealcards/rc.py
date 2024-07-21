from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)

        res = []

        for card in deck:
            if res:
                last_elm = res.pop()
                res.insert(0, last_elm)
            res.insert(0, card)

        return res

        