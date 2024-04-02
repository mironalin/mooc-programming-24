# Write your solution here
year = int(input("Year: "))
leap_year = year
while True:
    leap_year += 1

    if leap_year % 4 == 0 and leap_year % 100 == 0 and leap_year % 400 == 0:
        print(f"The next leap year after {year} is {leap_year}")
        break
    elif leap_year % 4 == 0 and leap_year % 100 != 0:
        print(f"The next leap year after {year} is {leap_year}")
        break
