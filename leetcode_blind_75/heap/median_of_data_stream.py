import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
      
    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap,-num)
        # print(num)

        while self.max_heap and len(self.max_heap) - len(self.min_heap) > 1:
            k = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,-k)

        while self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            k = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,-k)
        
        while self.min_heap and len(self.min_heap) > len(self.max_heap):
            k = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-k)

        
        # print(num,self.max_heap,self.min_heap)
        

    def findMedian(self) -> float:
        if not self.max_heap:
            return self.min_heap[0]
        
        if not self.min_heap:
            return -self.max_heap[0]

        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0])/2
        else:
            return -self.max_heap[0]