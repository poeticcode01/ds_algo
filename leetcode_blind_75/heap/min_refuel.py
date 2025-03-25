import heapq
from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # Max heap to store the available fuel
        max_heap = []
        stations.append((target, 0))  # Treat the destination as a station with 0 fuel

        fuel = startFuel  # Current fuel level
        stops = 0  # Number of refueling stops
        prev = 0  # Previous station position
        
        for pos, fuel_available in stations:
            fuel -= (pos - prev)  # Decrease fuel by the distance traveled
            
            # If we run out of fuel before reaching this station, refuel from max_heap
            while fuel < 0 and max_heap:
                fuel += -heapq.heappop(max_heap)  # Refuel from the station with the most fuel
                stops += 1
            
            # If we still can't reach the next station, return -1
            if fuel < 0:
                return -1
            
            heapq.heappush(max_heap, -fuel_available)  # Add station's fuel to the heap
            prev = pos  # Update previous station position
        
        return stops