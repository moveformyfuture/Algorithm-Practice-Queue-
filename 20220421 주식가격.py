# 1. len(price)를 활용해 0으로 구성된 Queue를 선언
# 2. 이중 for문을 활용해 가격의 증감을 비교

def solution(prices):
    answer = [0] * len(prices) # 시간을 0으로 구성된 Queue로 선언

    for i in range(len(prices)): # i = 0, 1, 2, 3, 4
        for j in range(i+1, len(prices)): # j = 1, 2, 3, 4
            if prices[i] <= prices[j]: # price의 첫번째 가격부터 그 이후의 가격과 증감 비교
                answer[i] += 1
            else: # 가격이 변한 경우
                answer[i] += 1
                break
    return answer