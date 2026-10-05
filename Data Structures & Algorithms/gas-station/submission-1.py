class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Basically just try and start, then go from there again

        def circuit(startIndex):
            fuel = 0
            moved = 0
            for i in range(len(gas)):
                moved += 1
                index = (startIndex + i) % len(gas)


                fuel -= cost[index]
                fuel += gas[index]

                if fuel < 0:
                    return [index, moved, False]
            
            return [startIndex, moved, True]

        point = 0
        while point < len(gas):
            newStart, toMove, success = circuit(point)
            if success:
                return point
            else:
                point += toMove

        return -1