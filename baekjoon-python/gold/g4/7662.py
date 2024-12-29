import sys
from collections import Counter
from heapq import heappush, heappop
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    command_length = int(input())
    min_heap = []
    max_heap = []
    counter = Counter()
    for _ in range(command_length):
        command, number = input().rstrip().split()
        if command == "I":
            heappush(min_heap, int(number))
            heappush(max_heap, -int(number))
            counter[int(number)] += 1
        elif command == "D":
            if number == "1":
                while max_heap and counter[-max_heap[0]] == 0:
                    heappop(max_heap)
                    
                if max_heap:
                    max_num = heappop(max_heap)
                    counter[-max_num] -= 1
            elif number == "-1":
                while min_heap and counter[min_heap[0]] == 0:
                    heappop(min_heap)
                    
                if min_heap:
                    min_num = heappop(min_heap)
                    counter[min_num] -= 1
                        
    while min_heap and counter[min_heap[0]] == 0:
        heappop(min_heap)
        
    while max_heap and counter[-max_heap[0]] == 0:
        heappop(max_heap)
    
    if len(min_heap) == 0 or len(max_heap) == 0:
        print("EMPTY")
    else:
        print(-max_heap[0], min_heap[0])