# 큐 관리 : 큐에서 하나씩 꺼내서 수행할 수 있으면 하고 아니면 다시 넣는다.
# 1. Queue를 만든다.
# 2. 나보다 중요한 job이 있으면 뒤에 넣는다.
# 3. 내가 제일 중요하다면 수행하고, location과 비교한다.

def solution(priorities, location):
    printer = [(i, p) for i, p in enumerate(priorities)]  # enumerate : 집합의 인덱스와 값을 반환함.
    turn = 0

    while printer:  # printer에 job이 남아있을 때까지 반복한다.
        job = printer.pop(0)  # pop(n) : 집합의 n번째 원소를 삭제하고, 반환함
        if any(job[1] < other_job[1] for other_job in printer): # any(수식) : 수식을 만족하는 경우가 하나라도 있는지 확인
            printer.append(job)
        else:
            turn += 1
            if job[0] == location:
                break;
    return turn