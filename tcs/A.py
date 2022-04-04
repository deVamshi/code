from datetime import timedelta, date
import calendar

inp, givenWeekday, n = list(input().split(" "))
n = int(n)
year = int(inp[0:4])
month = int(inp[4:6])
day = int(inp[6:])
givenWeekday = givenWeekday.lower()
def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True

dateGiven = date(year, month, day)
found = False
i = 1
came = False
while True:
    if givenWeekday == calendar.day_name[dateGiven.weekday()][0:3].lower():
        print("NO", 0)
        break
    if is_prime(i):
        updatedDate = date(year, month, day) + timedelta(days=i)

        if calendar.day_name[updatedDate.weekday()][0:3].lower() == givenWeekday: came = True

        if is_prime(updatedDate.month):
            found = True
    if found: break
    if came: i += 7
    else: i += 1

if found: print("YES" if i <= n else "NO", i)