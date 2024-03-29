'''
    구간 합
    연속적으로 나열된 N개의 수가 있을 때 특정 구간의 모든 수를 합한 값을 계산하는 문제
    예를 들어, 5개의 데이터로 구성된 수열 {10, 20, 30, 40, 50}이 있다고 가정했을 때
    두 번째 수부터 네 번째 수까지의 합은 20 + 30 + 40 = 90입니다.

    구간 합 빠르게 계산하기
     - N개의 정수로 구성된 수열이 있습니다.
     - M개의 쿼리 정보가 주어집니다.
       ㅇ 각 쿼리는 left와 right로 구성됩니다.
       ㅇ 각 쿼리에 대하여 [left, right]구간에 포함된 데이터들의 합을 출력해야합니다.
     - 수행 시간 제한은 O(N+M)입니다.

     접두사 합 : 배열의 맨 앞부터 특정 위치까지의 합을 미리 구해 놓은 것
     접두사 합을 활용한 알고리즘
       ㅇ N개의 수 위치 각각에 대하여 접두사 합을 계산하여 P에 저장합니다.
       ㅇ 매 M개의 쿼리 정보를 확인할 때 구간 합은 P[Right]-P[Left-1]입니다.
'''

# 데이터의 개수 N과 데이터 입력받기
n = 5
data = [10, 20, 30, 40, 50]

# 구간 합 계산(세 번째 수부터 네 번째 수까지)
def prefixsum(left, right):
    sum_value = 0
    prefix_sum = [0]
    for i in data:
        sum_value += i
        prefix_sum.append(sum_value)

    return prefix_sum[right] - prefix_sum[left - 1]

print(prefixsum(3, 4))
