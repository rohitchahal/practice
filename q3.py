input_file = open("data.txt", "r")
olympic_years = {}
for line in input_file:
    year, city = line.split()
    olympic_years[year] = city

input_file.close()
print(olympic_years)