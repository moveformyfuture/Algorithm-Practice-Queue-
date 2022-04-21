# 1. return 하고자 하는 것 확인 -> 변수 선언(초기화)
# 2. 순서가 바뀌는 것(bridge)에 대한 queue 생성
# 3. bridge 안에서의 트럭 대수(bridge length) 비교
# 4. bridge 안에서의 트럭 무게 (truck_weights) 비교

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0 for _ in range(bridge_length)] # range(n) : n-1 까지의 숫자를 생성
                                               # 비어있는 bridge를 0으로 표현

    while bridge:

        time += 1 # 시간 count
        bridge.pop(0) # queue에서 가장 앞의 차가 bridge로 들어간것 표현

        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight: # 다리 위의 차 무게합과 대기트럭의 무게 합 비교
                t = truck_weights.pop(0)
                bridge.append(t) # 다리를 통과함
            else:
                bridge.append(0) # 다리를 통과하지 못하면 0 추가해서 비어있는 bdirge 유지

    return time