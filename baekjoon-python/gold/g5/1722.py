import sys
import math
input = sys.stdin.readline

# k 번째 순열 찾기
def findKthSequence(k):
    # 찾을 순열
    sequence = []
    # 1부터 n까지 수열
    numbers = list(range(1, n + 1))
    
    # i: 체크할 순열 깊이
    for i in range(n - 1, -1, -1):
        # i 번째 깊이 구간의 크기
        case_size = math.factorial(i)
        # 몇 번째 index에 속하는 지 구하기
        # 이때 1번부터 case_size 번째가 한 구간이므로 case_size 번째인 경우 몫이 커져 다음 구간으로 넘어간다.
        # 따라서 k - 1을 해줘야 정확한 구간을 구할 수 있다.
        index = (k - 1) // case_size
        # 해당하는 숫자 찾아 정답 순열에 넣기
        sequence.append(numbers.pop(index))
        # 다음 깊이에서 몇 번째를 찾아야 하는 지 갱신.
        # 이때 나머지는 0부터 시작한다.
        # 따라서 나머지 + 1을 해줘야 정확한 차례를 구할 수 있다.
        k = (k - 1) % case_size + 1
        
    # 수열 배열을 문자열로 변경
    return ' '.join(map(str, sequence))

# 순열 순위 찾기
def findSequenceRank(sequence):
    # 찾을 순위
    rank = 1
    # 1부터 n까지 수열
    numbers = list(range(1, n + 1))
    
    # i: 순열 깊이
    for i in range(n - 1, -1, -1):
        # i 번째 깊이 구간의 크기
        case_size = math.factorial(i)
        # 현재 순열의 숫자가 남은 수열의 몇 번째인지 확인
        index = numbers.index(sequence[n - i + 1])
        # 수열에서 제거
        del numbers[index]
        # 현재 깊이에서 구간의 크기 x 구간의 번호를 순위에 더해준다.
        rank += case_size * index
        
    # 구한 순위 반환
    return rank

# 입력
n = int(input())
cmd = list(map(int, input().rstrip().split()))

answer = ""

# 문제 타입 구분
cmd_type = cmd[0]

# 소문제 1번
if cmd_type == 1:
    k = cmd[1]
    answer = findKthSequence(k)
        
# 소문제 2번
elif cmd_type == 2:
    sequence = cmd[1:]
    answer = findSequenceRank(sequence)
    
print(answer)