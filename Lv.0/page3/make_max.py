def make_max(numbers):
    numbers.sort()
    return numbers[0]*numbers[1] if numbers[0]*numbers[1] > numbers[-1]*numbers[-2] else numbers[-1]*numbers[-2] 

# 주어진 배열을 정렬 후
# 제일 작은 값 두 개가 - 이면, 곱했을 때 +이므로 최댓값 두 개의 곱과 비교.