import heapq

n = int(input())
heap = []

for i in range(n):
    numbers = list(map(int, input().split()))
    
    for number in numbers:
        if len(heap) < n:
            heapq.heappush(heap, number)
        else:
            if number > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, number)

print(heap[0])