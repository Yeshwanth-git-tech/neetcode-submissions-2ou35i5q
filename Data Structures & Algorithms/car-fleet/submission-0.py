class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for p, s in cars:
            time_to_arrive = (target - p) / float(s)
            if not stack or time_to_arrive > stack[-1]:
                stack.append(time_to_arrive)
        return len(stack)
