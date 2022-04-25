# 1. 시간이 1씩 계속 더해짐
# 2. 7초일때 첫번째 값의 연산이 필요함 -> cnt 더해
# 3. 7초일때 두번째 값의 연산 결과? --> cnt 더해
# 4. 7초일때 세번재 값의 연산 결과? --> cnt 초기화 & 정답에 추가
# 5. 위의 과정 반복
# 6. 마지막 cnt 정답에 추가

def solution(progresses, speeds):
    q = []
    time = 0
    cnt = 0

    while (len(progresses) > 0):
        if (progresses[0] + speeds[0] * time < 100):
            time += 1
            if (cnt > 0):
                q.append(cnt)
                cnt = 0

        else:
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
    q.append(cnt)
    return q