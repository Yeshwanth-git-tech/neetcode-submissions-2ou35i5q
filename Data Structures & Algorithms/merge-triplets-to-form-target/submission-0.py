class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            for i in range(len(t)):
                if t[i] == target[i]:
                    # good.add(t[i])
                    good.add(i)
        # store the index, not the value


        # good.add(t[i])    # current: stores the value
        # good.add(i)       # correct: stores the position

        # If the target has repeated values, the set collapses them.

        return len(good) == len(target)
        