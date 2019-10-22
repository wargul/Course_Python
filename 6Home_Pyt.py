#year , leap year

years = []
for year in range (1990, 2018):
    years.append(year)
print(years)

leap_years = []
for year in years:
    if not year%4:
        leap_years.append(year)
print(leap_years)

while True:
    y_year = int(input("Write the Year ..."))
    if leap_years.count(y_year) > 0:
        print(f"Yes {y_year} leap year ")
    else:
        print(f"No {y_year} not leap year ")
