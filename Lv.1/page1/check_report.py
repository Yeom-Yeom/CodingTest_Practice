from collections import defaultdict

def check_report(id_list,report,k):
    answer = []

    report = list(set(report))
    user = defaultdict(set)
    cnt = defaultdict(int)

    for r in report:
        a,b = r.split()
        user[a].add(b)
        cnt[b]+=1
    
    for i in id_list:
        result = 0
        for u in user[i] :
            if cnt[u] >= k:
                result +=1
        answer.append(result)
    return answer

# another solution
# def solution(id_list, report, k):
#   answer = [0]*len(id_list)
#   reports = {x : 0 for x in id_list}
#   for r in set(report):
#       reports[r.split()[1]] += 1
#   for r in set(report):
#       if reports[r.split()[1]] >= k:
#           answer[id_list.index(r.split()[0])] += 1
#   return answer