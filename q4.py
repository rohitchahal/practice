olympic = {}

for i in range(2):
    while True:
        try:
            city = input("please enter city name:")
            if city == "":
                print("please enter correct city name")
            year = input("please enter year name:")
            if (year < 1992) and (year > 2016):
                print("please enter correct year name")
        olympic[year] = city
        except ValueError:
            print("please enter correct value:")

out_file = open("datanew.txt", 'w')
for year in olympic:
    out_file.write(year)
    out_file.write(" ")
    out_file.write(olympic[year])
    out_file.write('\n')
out_file.close()
