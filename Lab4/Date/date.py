import datetime

def FiveDaysAgo():
    FiveDays = datetime.date.today() - datetime.timedelta(days = 5)
    return FiveDays

def YesterdayTodayTomorrow():
    Yesterday = datetime.date.today() - datetime.timedelta(days = 1)
    Today = datetime.date.today()
    Tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
    return f"Yesterday: {Yesterday} \nToday: {Today} \nTomorrow: {Tomorrow}"

def DropMicroseconds():
    today = datetime.datetime.now()
    today = str(today)
    WithoutMicrosecs = today.split(".")
    return WithoutMicrosecs[0]

def secsdelta():
    date1 = datetime.datetime.now()
    date2 = datetime.datetime.now() - datetime.timedelta(days = 19)
    delta = date2 - date1
    return delta.total_seconds() 

print(FiveDaysAgo())
print(YesterdayTodayTomorrow())
print(DropMicroseconds())
print(secsdelta())
