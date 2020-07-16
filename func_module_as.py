import datetime as dt

def module_show():
    module_type = dir(dt)
    print(module_type)

def date_now():
    return dt.datetime.now()

def remain_date():
    # print(dt.date.today())
    today = dt.date.today()
    # print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
    # print(dt.datetime.now().replace(month=12, day=25))
    return dt.datetime(2020,12,25) - dt.datetime.now()

remain_date()

def remain_date_input(nmonth=12, nday=25):
    # print(dt.date.today())
    today = dt.date.today()
    # print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
    # print(dt.datetime.now().replace(month=12, day=25))
    return dt.datetime(2020, nmonth, nday) - dt.datetime.now()

nmonth = int(input('원하는 달을 입력하시오. :'))
nday = int(input('원하는 날을 입력하시오. :'))
print(remain_date_input(nmonth, nday))