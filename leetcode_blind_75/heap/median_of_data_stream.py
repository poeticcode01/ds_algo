import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        # print(num,"min_heap",self.min_heap,"max_heap", self.max_heap)
        heapq.heappush(self.max_heap,-num)
        if (len(self.max_heap) - len(self.min_heap) > 1):
            k = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,-k)

        while len(self.max_heap) and len(self.min_heap) and (-self.max_heap[0]) > self.min_heap[0]:
            k = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,-k)
        
        while len(self.min_heap) > len(self.max_heap):
            k = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-k)

        # print(num,"min_heap",self.min_heap,"max_heap", self.max_heap)
        

    def findMedian(self) -> float:
        # print("find median" ,"min_heap",self.min_heap,"max_heap", self.max_heap)
        min_heap_size = len(self.min_heap)
        max_heap_size = len(self.max_heap)
        if min_heap_size == 0 and max_heap_size == 0:
            # print(1)
            return None
        else:
            # print(2)
            if min_heap_size == 0:
                return -self.max_heap[0]
            if max_heap_size == 0:
                return self.min_heap[0]
            
            if min_heap_size == max_heap_size:
                return (self.min_heap[0] - self.max_heap[0])/2
            else:
                # if len(self.min_heap) > len(self.max_heap):
                #     return self.min_heap[0]
                # else:
                return -self.max_heap[0]