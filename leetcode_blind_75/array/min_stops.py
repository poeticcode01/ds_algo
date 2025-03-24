from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        cur_pos = 0
        cur_fuel = startFuel
        stops_count = 0
        last_stop = 0
        last_pos =  -1
        while cur_fuel+last_stop < target:
            flag,new_pos, new_fuel = self.find_max_fuel_within_reachable_stations(last_stop,last_pos+1,cur_fuel,stations)
            if not flag:
                return -1
                
            stops_count +=1
            last_pos = new_pos
            cur_pos = new_pos
            cur_fuel = new_fuel
            if cur_pos < len(stations):
                last_stop = stations[cur_pos][0]

        return stops_count

    def find_max_fuel_within_reachable_stations(self,last_stop,cur_pos,cur_fuel,stations):
        
        max_fuel = cur_fuel
        new_pos =  cur_pos
        flag = False
        while cur_pos < len(stations) and cur_fuel >= (stations[cur_pos][0]-last_stop):
            flag = True
            new_fuel =  (cur_fuel - (stations[cur_pos][0] - last_stop)) + stations[cur_pos][1]
            if new_fuel >= max_fuel:
                max_fuel =  new_fuel
                new_pos = cur_pos
            cur_pos +=1
        return flag,new_pos, max_fuel
    
if __name__ == "__main__":
    target = 1000
    startFuel = 83
    stations = [[47,220],[65,1],[98,113],[126,196],[186,218],[320,205],[686,317],[707,325],[754,104],[781,105]]
    print(Solution().minRefuelStops(target,startFuel,stations))
