import func_module
import func_module_as

#func_module.module_show()

nowdate = func_module.date_now()
# print(nowdate)

# now_year = nowdate.year
# now_month = nowdate.month
# now_day = nowdate.day
# print('오늘은', now_year, '년', now_month, '월', now_day, '일입니다.')

print('오늘은 {}년 {}월 {}일입니다.'.format(nowdate.year,nowdate.month,nowdate.day))

x_mas = nowdate.replace(month = 12, day = 25)
date_x_mas = '오늘은 {}년 {}월 {}일입니다.'.format(x_mas.year,x_mas.month,x_mas.day)
print(date_x_mas)

ndate = func_module_as.date_now()
print(ndate)

func_module_as.remain_date()
re_date = func_module_as.remain_date_input(10,20)
print(re_date)