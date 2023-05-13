def calendar():
    T = int(input())
    for test_case in range(1,T+1):
        for date in list(map(str,input().split())):
            year = date[0:4]
            month = date[4:6]
            day = date[6:8]
        if month <= '00' or month > '12':
            print(f'#{test_case} -1')
        elif month == '01' or month == '03' or month == '05' or month == '07' or month == '08' or month == '10' or month == '12':
            if day > '31' or day <= '0':
                print(f'#{test_case} -1')
            else:
                print(f'#{test_case} {year}/{month}/{day}')
        elif month == '04' or month == '06' or month == '09' or month == '11':
            if day > '30' or day <= '0' :
                print(f'#{test_case} -1')
            else:
                print(f'#{test_case} {year}/{month}/{day}')
        elif month == '02':
            if day > '28' or day <= '0':
                print(f'#{test_case} -1')
            else:
                print(f'#{test_case} {year}/{month}/{day}')
        else:
            print(f'#{test_case} {year}/{month}/{day}')
calendar()