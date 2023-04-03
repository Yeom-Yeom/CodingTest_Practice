from collections import deque
def repaint(n,m,section):
    answer = 0
    section = deque(section)

    while section:
        start = section.popleft()

        while section and start+m > section[0]:
            section.popleft()
        answer+=1
    return answer

print(repaint(8,4,[2,3,6]))

# another solution
# def solution(n,m,section):
#   answer = 1
#   prev = section[0]
#   for sec in section:
#       if sec - prev >= m:
#           prev = sec
#           answer+=1
#   return answer