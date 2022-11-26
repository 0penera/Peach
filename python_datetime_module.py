import datetime
import pytz

#-------------------------------------
'''create date value'''
# d = datetime.date(2022, 7, 26)
# print(d)
# tday = datetime.date.today()
# print(tday.year)
# print(tday.month)
# print(tday.day)
# print(tday.weekday())
# print(tday.isoweekday())

#--------------------------------------
'''timedelta'''
# tday = datetime.date.today()
# tdelta = datetime.timedelta(days=7)
# print(tday + tdelta)
# print(tday - tdelta)
'''date2 = date1 + timedelta
    timedelta = date1 + date2'''
    
# bday = datetime.date(2015, 11, 11)
# till_bday = tday - bday
# print(till_bday)
# print(till_bday.total_seconds())

#---------------------------------------
'''time and datetime'''
# t = datetime.time(9, 30, 45, 10000)
# print(t)
# print(t.hour)

# dt = datetime.datetime(2022, 7, 24, 12, 32, 42, 100000)
# tdelta = datetime.timedelta(days=7)
# tdelta1 = datetime.timedelta(hours=7)
# print(dt)
# print(dt.time())
# print(dt.year)
# print(tdelta)
# print(dt - tdelta)
# print(dt - tdelta1)

#--------------------------------------
'''using pytz is recommended'''
# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# dt = datetime.datetime(2022, 7, 23, 1, 32, 0, 1000, tzinfo=pytz.UTC)
# print(dt)
# dt_now = datetime.datetime.now(tz=pytz.UTC)  #using this one
# print(dt_now)
# dt_now = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_now)

# dt_mtn = datetime.datetime.now(pytz.timezone('US/Mountain'))
# print(dt_mtn)
# dt_kor = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
# print(dt_kor)

#----------------------------------------------------------
'''find timezone'''
# for tz in pytz.all_timezones:
#     print(tz)
#----------------------------------------------------------
''''''
# dt_now = datetime.datetime.now(tz=pytz.UTC)
# print(dt_now)

# dt_mtn = datetime.datetime.now()
# print(dt_mtn)
# mtn_tz = pytz.timezone('US/Mountain')
# print(mtn_tz)
# dt_mtn = mtn_tz.localize(dt_mtn)
# print(dt_mtn)
# dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
# print(dt_east)

#------------------------------------------------------
'''print datetime format'''
dt_mtn = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul'))

print(dt_mtn.isoformat())
print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'July 26, 2016'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)