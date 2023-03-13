def num_str_and_eng(s):
    arr = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for a in arr : 
        if a in s:
            s = s.replace(a,str(arr.index(a)))
    return int(s)

# another solution
# def solution(s):
#   num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
#   answer = s
#   for key,value in num_dic.items():
#       answer = answer.replace(key,value)
#   return int(answer)