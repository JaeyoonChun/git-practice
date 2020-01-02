def input_date():
    year = int(input("__년도를 입력하시오:"))
    month = int(input("__월을 입력하시오:"))
    day = int(input("__일을 입력하시오:"))
    return year, month, day

def get_day_name(input_year, input_month, input_day):
    day_sum = 0
    monthly_numOfDay=(31,28,31,30,31,30,31,31,30,31,30,31)
    day_name=("일요일","월요일","화요일","수요일","목요일","금요일","토요일")
    
    leap_cnt = ((input_year-1)//4) - ((input_year-1)//100) + ((input_year-1)//400)
    normal_cnt = (input_year-1) - leap_cnt
    
    day_sum = (leap_cnt * 366) + (normal_cnt * 365)
    
    if not is_leap(input_year):
        for m in range(1, input_month):
            day_sum += monthly_numOfDay[m-1]
    else:
        for m in range(1, input_month):
            if m != 2:
                day_sum += monthly_numOfDay[m-1]
            else:
                day_sum += 29
    
    day_sum += input_day
    idx = day_sum%7
    
    return day_name[idx]
    
def is_leap(input_year):
    if input_year%4 == 0:
        if input_year%400 == 0:
            return True
        elif input_year%100!=0:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    year, month, day = input_date()
    day_name = get_day_name(year, month, day)
    print(day_name)
    if is_leap(year) == True:
        print("입력하신 %s은 윤년입니다" %year)

    print("git diff : 수정사항 입력")
