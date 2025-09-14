from collections import defaultdict, deque

class RequestHandler:
    def __init__(self):
        self.request_counter = defaultdict(int)   # per second request counts
        self.timestamp_list = deque()             # maintain order of timestamps
    
    def addRequest(self, timestamp):
        time_sec = timestamp // 1000
        
        # record request
        self.request_counter[time_sec] += 1
        
        # append timestamp if it's new
        if not self.timestamp_list or self.timestamp_list[-1] != time_sec:
            self.timestamp_list.append(time_sec)
        
        # cleanup old timestamps beyond 300 sec window
        self.garbage_collector(time_sec)
    
    def getRequestCount(self, timestamp):
        time_sec = timestamp // 1000
        prev_time = time_sec - 300
        
        # cleanup first
        self.garbage_collector(time_sec)
        
        # sum requests in the last 300 seconds
        count = 0
        for t in self.timestamp_list:
            if t > prev_time:
                count += self.request_counter[t]
        
        return count
    
    def garbage_collector(self, current_time):
        # remove timestamps older than 300 seconds
        while self.timestamp_list and self.timestamp_list[0] <= current_time - 300:
            old_time = self.timestamp_list.popleft()
            del self.request_counter[old_time]


if __name__ == "__main__":
    handler = RequestHandler()

    # simulate requests
    handler.addRequest(1000)   # 1s
    handler.addRequest(2000)   # 2s
    handler.addRequest(301000) # 301s

    print(handler.getRequestCount(302000)) 
