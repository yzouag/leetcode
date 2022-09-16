from collections import defaultdict, deque
from typing import List
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # if source == target:
        #     return 0

        # routes = list(map(set, routes))
        # # construct adjacent list
        # adjacent_list = defaultdict(set)
        # for i in range(len(routes)):
        #     for j in range(i+1, len(routes)):
        #         for stop in routes[i]:
        #             if stop in routes[j]:
        #                 adjacent_list[i].add(j)
        #                 adjacent_list[j].add(i)
        #                 break
        
        # # get all source bus and target bus
        # bus_source = deque([])
        # seen = set()
        # bus_target = set()
        # for bus_id, route in enumerate(routes):
        #     if source in route:
        #         bus_source.append((bus_id, 1))
        #         seen.add(bus_id)
        #     if target in route:
        #         bus_target.add(bus_id)
        
        # # breadth first search
        # while bus_source:
        #     bus_id, count = bus_source.popleft()
        #     if bus_id in bus_target:
        #         return count
        #     for neighbor_bus in adjacent_list[bus_id]:
        #         if neighbor_bus not in seen:
        #             bus_source.append((neighbor_bus, count+1))
        #             seen.add(neighbor_bus)
        # return -1

        to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                to_routes[j].add(i)
        bfs = [(source, 0)]
        seen = set([source])
        for stop, bus in bfs:
            if stop == target: return bus
            for i in to_routes[stop]:
                for j in routes[i]:
                    if j not in seen:
                        bfs.append((j, bus + 1))
                        seen.add(j)
                routes[i] = []  # seen route
        return -1

if __name__ == "__main__":
    routes = [[1,2,7],[3,6,7]]
    source = 1
    target = 6
    assert Solution().numBusesToDestination(routes, source, target) == 2

    routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
    source = 15
    target = 12
    assert Solution().numBusesToDestination(routes, source, target) == -1

    routes = [[1,7],[3,5]]
    source = 5
    target = 5
    assert Solution().numBusesToDestination(routes, source, target) == 0