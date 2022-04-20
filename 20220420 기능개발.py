# 문제 단순화
# 수식 : progresses[0] + time*speeds[0] -> time을 고려
# 1. 100을 초과하는 경우 :
    # (1) count를 answer에 반환
    # (2) 첫번째 원소 삭제
# 2. 100을 초과하지 않는 경우 :
    # (1) time을 늘려가며 반복


def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0) # pop(n) : n번째 항목을 삭제하고, 그 항목을 반환함(n 지정 안하면 마지막꺼로 지정됨)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer