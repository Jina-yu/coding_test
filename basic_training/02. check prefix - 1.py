from collections import deque

def solution(my_string, is_prefix):
    result = deque(my_string)
    answer = []
    while True:
        if not result:
            return 0
        left = result.popleft()
        answer.append(left)
        string = "".join(answer)
        if string == is_prefix:
            return 1
        elif string[0] != is_prefix[0]:
            return 0