import sys
input = sys.stdin.readline

n, k = map(int, input().split())
sequences = list(range(1, n + 1))
josephus = []
index = 0
while sequences:
    index = (index + k - 1) % len(sequences)
    josephus.append(sequences[index])
    del sequences[index]


print(str(josephus).replace('[', '<').replace(']', '>'))
