def exchange_student():
    T = int(input())
    for tc in range(1,T+1):
        n = int(input())
        day = list(map(int,input().split()))
        firstdayList = []
        for i in range(len(day)):
            if day[i] == 1:
                firstdayList.append(i)
        
        ans = 1e9
        for d in firstdayList:
            dayCnt = 0
            classCnt = 0
            
            while classCnt < n:
                if day[d] == 1:
                    classCnt+=1
                dayCnt+=1
                if d > 5 :
                    d = 0
                else: d+=1
            ans = min(ans,dayCnt)
        print(f'#{tc} {ans}') 
exchange_student()

