def is_year_leap(year):
    return year % 4 == 0
years_check = [2024, 2023]
for year in years_check:
    result = is_year_leap(year)
    print(f"год {year}: {result}")
