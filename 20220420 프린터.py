# 1. pop, get 사용
# 2. queue 만들기 : priorities가 사실상 대기행렬임.
# 3. return = location이 출력되는 순서 = turn
# 4. 작업에 대한 정의
#    (1) printer에서 꺼낸다(pop)
#    (2) 우선순위를 비교한다. (any)
#    (3) 우선순위가 높은게 있으면 다시 집어넣는다. (append)
#    (4) 우선순위가 높은게 없다면 출력한다. (출력 횟수 turn 증가)
#    (5) 출력하는 것 중 location과 idx가 동일한지 확인한다.

def solution(priorities, location):
    printer = [(i, p) for i, p in enumerate(priorities)]
    turn = 0

    while (len(printer) > 0):
        job = printer.pop(0)  # 대기행렬 printer의 0번째를 삭제 & 반환
        if any(job[1] < other_job[1] for other_job in printer):  # any(수식) : 하나라도 있다면 True 반환
            printer.append(job)  # job[1] : printer의 idx를 반환
        else:
            turn += 1
            if job[0] == location:
                break
    return turn