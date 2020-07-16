import datetime

def module_show():
    module_type = dir(datetime)
    print(module_type)

def date_now():
    return datetime.datetime.now()