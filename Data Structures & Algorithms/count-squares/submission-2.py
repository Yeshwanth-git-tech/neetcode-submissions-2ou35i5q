from collections import defaultdict
class CountSquares:
    def __init__(self):
        self.cnt = defaultdict(int)
        self.points = []
        

    def add(self, point: List[int]) -> None:
        x , y = point
        self.cnt[(x,y)]+=1
        self.points.append((x , y))

    def count(self, point: List[int]) -> int:

        res = 0
        qx , qy = point

        for x , y in self.points:
            if (abs(qy-y)!= abs(qx-x) or  (x == qx and y == qy)):
                continue
            res+= self.cnt[(qx , y)] * self.cnt[(x , qy)]

        return res
            
