from datetime import date
def getkey(d, target):
    for key, val in d.items():
        if val == target:
            return(key)
            break

d_start, m_start, y_start = map(str, input().split())
d_end, m_end, y_end = map(str, input().split())
d_start = int(d_start)
m_start = getkey(months, m_start)
# print(m_start)
y_start = int(y_start)

d_end = int(d_end)
m_end = getkey(months, m_end)
# print(m_end)
y_end = int(y_end)


birth_date = date(y_start, m_start, d_start)
current_date = date(y_end, m_end, d_end)

sday = []

for year in range(y_start, y_end + 1):
    this_year_birthday = date(year, m_start, d_start)
    
    if birth_date <= this_year_birthday <= current_date:

        if this_year_birthday.weekday() == 6:
            sday.append(year)
print(len(sday))
if sday:
    print(*(sday))
else:
    print()
