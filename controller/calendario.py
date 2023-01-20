#REF: https://docs.python.org/3/library/calendar.html#calendar.Calendar

from calendar import monthrange
import calendar

cal = calendar.Calendar(firstweekday=6)

DIAS_DA_SEMANA = ("MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY")

diasEmUmMes = monthrange(2011, 2)

#calDays = cal.monthdayscalendar(2022, 12)
calDays = cal.monthdatescalendar(2022, 12)

aux = 0

for weeks in calDays:
    print(DIAS_DA_SEMANA[aux])
    aux += 1
    for days in weeks:
        print(days)
    