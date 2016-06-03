# for year in range(1992, 2017, 4):
#     print(year,end='  ')
olympic_years = {"1992": "Barcelona", "1996": "Atlanta", "2000": "sydney", "2004": "Athens", "2008": "Beijing",
                 "2012": "London",
                 "2016": "Brazil"}
input_year = input("Please enter olympic year between 1992 and 2016 like 1992 or 1996 upto 2016")
while input_year not in olympic_years:
    print("Please enter correct year")
    input_year = input("Please enter olympic year between 1992 and 2016 like 1992 or 1996 up to 2016")

print("olympic held in ", olympic_years[input_year])
