def weapon_of_knight(number,limit,power):
    knight = []
    answer = 0
    for i in range(1,number+1):
        tmp = []
        for j in range(1,int(i**(1/2))+1):
            if i%j==0:
                tmp.append(i)
                if (j**2) != i:
                    tmp.append(i//j)
        knight.append(len(tmp))
    for k in knight:
        if k > limit:
            answer+=power
        else:
            answer+=k

    return answer

# another solution
# def cf(n): # 공약수 출력
#   a = []
#   for i in range(1,int(n**0.5)+1):
#       if n%i == 0:
#           a.append(n//i)
#           a.append(i)
#   return len(set(a))

# def solution(number,limit,power):
#   return sum([cf(i) if cf(i) <=limit else power for i in range(1,number+1)])