class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        # Cant we just iterate from the front, by taking time to destination and comparing with the car in front? then if smaller, then it joins the fleet
        n = len(position)
        ttd = [0] * n
        ttd[-1] = (target - position[-1]) // speed[-1]
        for i in range(len(position)-2, -1, -1):
            ttd[i] = (target - position[i]) // speed[i]

            if ttd[i] < ttd[i+1]: # We must update to match with the one in front
                ttd[i] = ttd[i+1] # They will arrive at the same time (because they are the same fleet)
            
        return len(set(ttd))
        # This was dumb, due to i misunderstood and thought in my head that the ordering inside of positions was the order of the cars
        """ 

        n = len(position)
        position, speed = zip(*sorted(zip(position, speed)))

        ttd = [0] * n
        ttd[-1] = (target - position[-1]) / speed[-1]
        for i in range(len(position)-2, -1, -1):
            ttd[i] = (target - position[i]) / speed[i]

            if ttd[i] < ttd[i+1]: # We must update to match with the one in front
                ttd[i] = ttd[i+1] # They will arrive at the same time (because they are the same fleet)
            
        return len(set(ttd))
