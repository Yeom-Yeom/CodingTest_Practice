def sum_of_consecutive_subseqeunces(sequence, k):
    answer = []
    sum = 0
    l = 0
    r = -1

    while True:
        if sum < k:
            r += 1
            if r >= len(sequence):
                break
            sum += sequence[r]
        else:
            sum -= sequence[l]
            if l>= len(sequence):
                break
            l += 1
        if sum == k:
            answer.append([l,r])
    answer.sort(key = lambda x: (x[1]-x[0], x[0]))
    return answer[0]

sum_of_consecutive_subseqeunces([1,2,3,4,5],7)